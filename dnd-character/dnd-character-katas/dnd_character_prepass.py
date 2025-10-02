"""
Dungeons & Dragons Character Generator - Problem Solving Methodology

This module demonstrates a systematic approach to analyzing problems and 
choosing appropriate implementation patterns.
"""

# ruff: noqa
# pylint: disable-all
# type: ignore

# =============================================================================
# STEP 1: PROBLEM ANALYSIS - EXTRACT REQUIREMENTS
# =============================================================================

"""
🔍 HOW TO RECOGNIZE REQUIREMENTS FROM PROBLEM DESCRIPTION:

📋 REQUIREMENT TYPES TO LOOK FOR:
1. Data Requirements → What things need to be stored/tracked?
2. Behavioral Requirements → What actions/processes need to happen?  
3. Business Rules → What calculations/constraints apply?
4. Examples → Concrete scenarios that illustrate the rules

🔍 KEY PHRASES THAT SIGNAL REQUIREMENTS:
- "This character has..." → Data requirements
- "You do this by..." → Process requirements
- "Formula: X + Y" → Calculation requirements  
- "For example..." → Validation examples

APPLIED TO D&D CHARACTER:

🎯 REQUIREMENT 1: Character Class with Six Attributes
FOUND IN README: "This character has, among other things, six abilities; 
strength, dexterity, constitution, intelligence, wisdom and charisma."
PATTERN: NOUNS that represent data/state the system needs to track.

🎯 REQUIREMENT 2: Ability Score Generation Algorithm  
FOUND IN README: "You do this by rolling four 6-sided dice and recording 
the sum of the largest three dice. You do this six times, once for each ability."
PATTERN: PROCEDURAL DESCRIPTIONS that describe HOW something works.

🎯 REQUIREMENT 3: Constitution Modifier and Hit Points
FOUND IN README: "Your character's initial hitpoints are 10 + your character's 
constitution modifier. You find your character's constitution modifier by 
subtracting 10 from your character's constitution, divide by 2 and round down."
PATTERN: MATHEMATICAL FORMULAS and DEPENDENT CALCULATIONS.
"""

# =============================================================================
# STEP 2: SOLUTION PATTERNS - MAP REQUIREMENTS TO IMPLEMENTATIONS
# =============================================================================

"""
🛠️ REQUIREMENT TYPE → IMPLEMENTATION PATTERN

📊 DATA REQUIREMENTS ("This character has...")
→ SOLUTION: Class with attributes
→ PATTERN: 
  class Character:
      def __init__(self):
          self.attribute1 = value
          self.attribute2 = value

🔄 PROCESS REQUIREMENTS ("You do this by..." / "Algorithm:")
→ SOLUTION: Method or function
→ DECISION CRITERIA:
  - If process belongs to an object → instance method
  - If process is independent → standalone function
  - If process creates objects → class method/constructor

🧮 CALCULATION REQUIREMENTS ("Formula: X + Y")
→ SOLUTION: Pure function (no side effects)
→ PATTERN:
  def calculate_something(input_value):
      result = formula_here
      return result

🎲 RANDOM/VARIABLE REQUIREMENTS ("randomly determined", "rolling dice")
→ SOLUTION: Use random module + appropriate data structures
→ PATTERN:
  import random
  values = [random.operation() for _ in range(count)]

🔗 DEPENDENCY REQUIREMENTS ("A depends on B", "A is calculated from B")
→ SOLUTION: Calculate in correct order, pass dependencies as parameters
→ PATTERN:
  b_value = calculate_b()
  a_value = calculate_a(b_value)

📝 COLLECTION REQUIREMENTS ("six abilities", "multiple items")
→ SOLUTION: Lists, tuples, or multiple attributes
→ DECISION CRITERIA:
  - Fixed set → individual attributes or tuple
  - Variable set → list or dictionary
"""

# =============================================================================
# STEP 3: DESIGN DECISIONS - WHY CHOOSE SPECIFIC APPROACHES
# =============================================================================

"""
🎯 DECISION FRAMEWORK:
1. Is it DATA? → Class attribute or variable
2. Is it BEHAVIOR? → Method or function  
3. Is it PURE CALCULATION? → Standalone function
4. Is it OBJECT-SPECIFIC? → Instance method
5. Is it RANDOM/VARIABLE? → Use random module
6. Does it DEPEND on other values? → Calculate dependencies first

APPLIED TO D&D CHARACTER:

WHY ability() IS AN INSTANCE METHOD:
- Belongs to each character instance (object-specific behavior)
- Generates unique values per character
- Part of character creation process
- Called as self.ability() during __init__

WHY modifier() IS A STANDALONE FUNCTION:
- Pure mathematical calculation (stateless)
- Same input → same output (no side effects)
- Universal D&D rule applicable to all entities
- Reusable beyond just the Character class

DESIGN PATTERN SUMMARY:
- Instance-specific behavior → instance method
- Universal calculations → standalone function
"""

# =============================================================================
# STEP 4: IMPLEMENTATION DETAILS
# =============================================================================

"""
🔧 CONCRETE IMPLEMENTATION CHOICES:

REQUIREMENT 1: Six Attributes
SOLUTION: Individual attributes (not dictionary/list)
REASONING: Fixed set, each has semantic meaning, direct access needed

REQUIREMENT 2: Dice Rolling Algorithm  
SOLUTION: Instance method with generator expression + sorted() + slicing
REASONING: Belongs to character, needs randomness, elegant algorithm

REQUIREMENT 3: Modifier Calculation
SOLUTION: Pure function with floor division
REASONING: Universal rule, stateless, reusable

KEY TECHNICAL DETAILS:
1. Use random.randint(1, 6) for dice rolls
2. Use sorted() + slicing [1:] to drop lowest die  
3. Use floor division (//) for modifier calculation
4. Calculate hitpoints in __init__ after constitution is set
5. Use constants for magic numbers (dice count, sides)

MODIFIER EXAMPLES FOR VALIDATION:
Constitution Score → Modifier
8-9   → -1
10-11 → +0 (baseline)
12-13 → +1
14-15 → +2
16-17 → +3
18-19 → +4
"""

# =============================================================================
# STEP 5: ANTI-PATTERNS TO AVOID
# =============================================================================

"""
💡 COMMON MISTAKES IN PROBLEM-TO-SOLUTION MAPPING:

❌ OVER-ENGINEERING:
- Making everything a class when simple functions suffice
- Using complex patterns for simple problems
- Adding unnecessary abstractions

❌ UNDER-ENGINEERING:  
- Making everything global functions
- Not using classes when state management is needed
- Ignoring code organization

❌ MIXING CONCERNS:
- Putting pure calculations inside stateful objects
- Mixing data and behavior inappropriately
- Not separating different types of logic

❌ DEPENDENCY ISSUES:
- Not considering calculation order
- Circular dependencies between components
- Hardcoding values that should be configurable

✅ GOOD PRACTICES:
- Match solution complexity to problem complexity
- Separate data, behavior, and calculations appropriately
- Consider reusability and testability
- Follow single responsibility principle
"""

