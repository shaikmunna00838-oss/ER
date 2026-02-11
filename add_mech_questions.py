from app import app, db, Question

mech_questions = [
    {"question": "Unit of force?", "option_a": "Newton", "option_b": "Pascal", "option_c": "Joule", "option_d": "Watt", "correct_option": "A"},
    {"question": "Unit of pressure?", "option_a": "Newton", "option_b": "Pascal", "option_c": "Joule", "option_d": "Watt", "correct_option": "B"},
    {"question": "Unit of work?", "option_a": "Newton", "option_b": "Pascal", "option_c": "Joule", "option_d": "Watt", "correct_option": "C"},
    {"question": "Unit of power?", "option_a": "Newton", "option_b": "Pascal", "option_c": "Joule", "option_d": "Watt", "correct_option": "D"},
    {"question": "First law of thermodynamics is?", "option_a": "Energy cannot be created or destroyed", "option_b": "Entropy of universe always increases", "option_c": "F=ma", "option_d": "P=VI", "correct_option": "A"},
    {"question": "Second law of thermodynamics states?", "option_a": "Energy conserved", "option_b": "Entropy increases", "option_c": "Force=mass*acceleration", "option_d": "Pressure is force/unit area", "correct_option": "B"},
    {"question": "Which engine uses spark ignition?", "option_a": "Diesel engine", "option_b": "Petrol engine", "option_c": "Steam engine", "option_d": "Gas turbine", "correct_option": "B"},
    {"question": "Which engine uses compression ignition?", "option_a": "Diesel engine", "option_b": "Petrol engine", "option_c": "Steam engine", "option_d": "Gas turbine", "correct_option": "A"},
    {"question": "Stress formula?", "option_a": "F/A", "option_b": "A/F", "option_c": "F*L", "option_d": "L/F", "correct_option": "A"},
    {"question": "Strain formula?", "option_a": "ΔL/L", "option_b": "L/ΔL", "option_c": "F/A", "option_d": "A/F", "correct_option": "A"},
    {"question": "Young's modulus formula?", "option_a": "Stress/Strain", "option_b": "Strain/Stress", "option_c": "Force*Area", "option_d": "ΔL/L", "correct_option": "A"},
    {"question": "Shear stress formula?", "option_a": "F/A", "option_b": "V/A", "option_c": "ΔL/L", "option_d": "P/A", "correct_option": "B"},
    {"question": "Thermal conductivity unit?", "option_a": "W/m·K", "option_b": "J/s", "option_c": "Pa", "option_d": "N", "correct_option": "A"},
    {"question": "Heat capacity unit?", "option_a": "J/K", "option_b": "W", "option_c": "Pa", "option_d": "N", "correct_option": "A"},
    {"question": "Efficiency formula?", "option_a": "Output/Input", "option_b": "Input/Output", "option_c": "Work/Power", "option_d": "Power/Work", "correct_option": "A"},
    {"question": "Ideal gas law?", "option_a": "PV=nRT", "option_b": "F=ma", "option_c": "E=mc^2", "option_d": "P=VI", "correct_option": "A"},
    {"question": "Which gear increases speed?", "option_a": "Smaller gear driving larger", "option_b": "Larger gear driving smaller", "option_c": "Equal gears", "option_d": "None", "correct_option": "B"},
    {"question": "Which gear increases torque?", "option_a": "Smaller driving larger", "option_b": "Larger driving smaller", "option_c": "Equal gears", "option_d": "None", "correct_option": "A"},
    {"question": "Flywheel is used for?", "option_a": "Store energy", "option_b": "Convert energy", "option_c": "Reduce speed", "option_d": "Increase friction", "correct_option": "A"},
    {"question": "Clutch is used for?", "option_a": "Engage/disengage engine", "option_b": "Increase torque", "option_c": "Store energy", "option_d": "Measure speed", "correct_option": "A"},
    {"question": "Cam converts?", "option_a": "Rotary to reciprocating motion", "option_b": "Linear to rotary", "option_c": "Torque to power", "option_d": "Speed to torque", "correct_option": "A"},
    {"question": "Crankshaft converts?", "option_a": "Reciprocating to rotary motion", "option_b": "Rotary to reciprocating", "option_c": "Torque to power", "option_d": "Speed to torque", "correct_option": "A"},
    {"question": "Belt drive is used for?", "option_a": "Transmit motion between shafts", "option_b": "Increase speed", "option_c": "Store energy", "option_d": "Measure torque", "correct_option": "A"},
    {"question": "Shaft transmits?", "option_a": "Torque", "option_b": "Voltage", "option_c": "Current", "option_d": "Energy only", "correct_option": "A"},
    {"question": "Bearing reduces?", "option_a": "Friction", "option_b": "Torque", "option_c": "Speed", "option_d": "Force", "correct_option": "A"},
    {"question": "Poisson's ratio formula?", "option_a": "Lateral strain/Longitudinal strain", "option_b": "Stress/Strain", "option_c": "ΔL/L", "option_d": "F/A", "correct_option": "A"},
    {"question": "Shear strain formula?", "option_a": "Tan θ", "option_b": "Sin θ", "option_c": "Cos θ", "option_d": "θ", "correct_option": "A"},
    {"question": "Torque formula?", "option_a": "F × r", "option_b": "F / r", "option_c": "P × t", "option_d": "W / t", "correct_option": "A"},
    {"question": "Power in rotational motion?", "option_a": "Torque × angular velocity", "option_b": "Force × velocity", "option_c": "Work / time", "option_d": "Energy × time", "correct_option": "A"},
    {"question": "Velocity ratio of machine?", "option_a": "Input speed/Output speed", "option_b": "Output speed/Input speed", "option_c": "Torque ratio", "option_d": "Work ratio", "correct_option": "A"},
    {"question": "Mechanical advantage?", "option_a": "Output force/Input force", "option_b": "Input force/Output force", "option_c": "Work ratio", "option_d": "Velocity ratio", "correct_option": "A"},
    {"question": "Efficiency of machine?", "option_a": "Mechanical advantage/Velocity ratio", "option_b": "Velocity ratio/Mechanical advantage", "option_c": "Power ratio", "option_d": "Work ratio", "correct_option": "A"},
    {"question": "Simple machine examples?", "option_a": "Lever, Pulley, Inclined plane", "option_b": "Motor, Generator", "option_c": "Compressor, Pump", "option_d": "Engine, Gearbox", "correct_option": "A"},
    {"question": "Conservation of energy in mechanics?", "option_a": "Total energy remains constant", "option_b": "Energy lost", "option_c": "Energy increases", "option_d": "None", "correct_option": "A"},
    {"question": "Centrifugal force acts?", "option_a": "Outward from center", "option_b": "Toward center", "option_c": "Perpendicular", "option_d": "Parallel", "correct_option": "A"},
    {"question": "Centripetal force acts?", "option_a": "Toward center", "option_b": "Outward from center", "option_c": "Perpendicular", "option_d": "Parallel", "correct_option": "A"},
    {"question": "Velocity in circular motion?", "option_a": "Tangential", "option_b": "Radial", "option_c": "Zero", "option_d": "Constant", "correct_option": "A"},
    {"question": "Acceleration in circular motion?", "option_a": "Centripetal", "option_b": "Tangential", "option_c": "Zero", "option_d": "Linear", "correct_option": "A"},
    {"question": "Work done in circular motion?", "option_a": "Zero", "option_b": "Non-zero", "option_c": "Depends", "option_d": "Infinite", "correct_option": "A"},
    {"question": "Impulse formula?", "option_a": "F × t", "option_b": "m × v", "option_c": "1/2 m v^2", "option_d": "P × V", "correct_option": "A"},
    {"question": "Impact of body is measured in?", "option_a": "Impulse", "option_b": "Force", "option_c": "Energy", "option_d": "Power", "correct_option": "A"},
    {"question": "Hydraulic machine works on?", "option_a": "Pascal's law", "option_b": "Newton's law", "option_c": "Ohm's law", "option_d": "Hooke's law", "correct_option": "A"},
    {"question": "Compressor increases?", "option_a": "Pressure of fluid", "option_b": "Velocity of fluid", "option_c": "Volume", "option_d": "None", "correct_option": "A"},
    {"question": "Pump increases?", "option_a": "Pressure of fluid", "option_b": "Velocity of fluid", "option_c": "Volume", "option_d": "None", "correct_option": "A"},
    {"question": "Heat engine converts?", "option_a": "Heat to work", "option_b": "Work to heat", "option_c": "Kinetic to potential", "option_d": "None", "correct_option": "A"},
    {"question": "Steam turbine is?", "option_a": "Rotary machine", "option_b": "Reciprocating machine", "option_c": "Linear machine", "option_d": "None", "correct_option": "A"},
    {"question": "Refrigeration works on?", "option_a": "Vapor compression cycle", "option_b": "Gas cycle", "option_c": "Thermal cycle", "option_d": "None", "correct_option": "A"}
]

with app.app_context():
    for q in mech_questions:
        existing = Question.query.filter_by(question=q["question"]).first()
        if not existing:  # prevent duplicates
            question = Question(
                department="MECH",
                question=q["question"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"]
            )
            db.session.add(question)
    db.session.commit()
    print("✅ All 50 MECH Questions Added Successfully!")
