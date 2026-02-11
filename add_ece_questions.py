from app import app, db, Question

ece_questions = [
    {"question": "The basic unit of digital electronics is?", "option_a": "Resistor", "option_b": "Transistor", "option_c": "Diode", "option_d": "Logic Gate", "correct_option": "D"},
    {"question": "Binary number system uses how many digits?", "option_a": "2", "option_b": "8", "option_c": "10", "option_d": "16", "correct_option": "A"},
    {"question": "Which device converts AC to DC?", "option_a": "Rectifier", "option_b": "Inverter", "option_c": "Transformer", "option_d": "Oscillator", "correct_option": "A"},
    {"question": "Unit of capacitance?", "option_a": "Ohm", "option_b": "Farad", "option_c": "Henry", "option_d": "Volt", "correct_option": "B"},
    {"question": "Unit of inductance?", "option_a": "Ohm", "option_b": "Henry", "option_c": "Farad", "option_d": "Volt", "correct_option": "B"},
    {"question": "Which logic gate is called inverter?", "option_a": "AND", "option_b": "OR", "option_c": "NOT", "option_d": "NAND", "correct_option": "C"},
    {"question": "Which device converts DC to AC?", "option_a": "Rectifier", "option_b": "Inverter", "option_c": "Transformer", "option_d": "Amplifier", "correct_option": "B"},
    {"question": "The speed of light in vacuum?", "option_a": "3x10^8 m/s", "option_b": "3x10^6 m/s", "option_c": "3x10^3 m/s", "option_d": "3x10^5 m/s", "correct_option": "A"},
    {"question": "Semiconductor used in LEDs?", "option_a": "Silicon", "option_b": "Gallium Arsenide", "option_c": "Germanium", "option_d": "Copper", "correct_option": "B"},
    {"question": "Which filter passes low frequencies?", "option_a": "Low Pass", "option_b": "High Pass", "option_c": "Band Pass", "option_d": "Band Stop", "correct_option": "A"},
    {"question": "Which filter passes high frequencies?", "option_a": "Low Pass", "option_b": "High Pass", "option_c": "Band Pass", "option_d": "Band Stop", "correct_option": "B"},
    {"question": "Ohm's Law formula?", "option_a": "V=IR", "option_b": "P=VI", "option_c": "I=V^2/R", "option_d": "V=I^2R", "correct_option": "A"},
    {"question": "Digital signal has?", "option_a": "Continuous values", "option_b": "Discrete values", "option_c": "Random values", "option_d": "Analog values", "correct_option": "B"},
    {"question": "Analog signal has?", "option_a": "Continuous values", "option_b": "Discrete values", "option_c": "Digital values", "option_d": "Binary values", "correct_option": "A"},
    {"question": "Which logic gate output is high only if all inputs are high?", "option_a": "AND", "option_b": "OR", "option_c": "NAND", "option_d": "NOR", "correct_option": "A"},
    {"question": "Which logic gate output is high if at least one input is high?", "option_a": "AND", "option_b": "OR", "option_c": "NAND", "option_d": "NOR", "correct_option": "B"},
    {"question": "NAND gate is universal?", "option_a": "Yes", "option_b": "No", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "NOR gate is universal?", "option_a": "Yes", "option_b": "No", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Binary equivalent of decimal 10?", "option_a": "1010", "option_b": "1100", "option_c": "1001", "option_d": "1110", "correct_option": "A"},
    {"question": "Binary equivalent of decimal 15?", "option_a": "1111", "option_b": "1101", "option_c": "1011", "option_d": "1001", "correct_option": "A"},
    {"question": "Which modulation uses amplitude variation?", "option_a": "AM", "option_b": "FM", "option_c": "PM", "option_d": "Pulse", "correct_option": "A"},
    {"question": "Which modulation uses frequency variation?", "option_a": "AM", "option_b": "FM", "option_c": "PM", "option_d": "Pulse", "correct_option": "B"},
    {"question": "Unit of frequency?", "option_a": "Hertz", "option_b": "Volt", "option_c": "Ampere", "option_d": "Ohm", "correct_option": "A"},
    {"question": "Unit of current?", "option_a": "Volt", "option_b": "Ampere", "option_c": "Ohm", "option_d": "Henry", "correct_option": "B"},
    {"question": "Unit of voltage?", "option_a": "Volt", "option_b": "Ampere", "option_c": "Ohm", "option_d": "Farad", "correct_option": "A"},
    {"question": "Which component stores energy in magnetic field?", "option_a": "Capacitor", "option_b": "Inductor", "option_c": "Resistor", "option_d": "Diode", "correct_option": "B"},
    {"question": "Which component stores energy in electric field?", "option_a": "Capacitor", "option_b": "Inductor", "option_c": "Resistor", "option_d": "Transistor", "correct_option": "A"},
    {"question": "Which device converts electrical energy to mechanical energy?", "option_a": "Motor", "option_b": "Generator", "option_c": "Rectifier", "option_d": "Amplifier", "correct_option": "A"},
    {"question": "Which device converts mechanical energy to electrical energy?", "option_a": "Motor", "option_b": "Generator", "option_c": "Rectifier", "option_d": "Amplifier", "correct_option": "B"},
    {"question": "The color code of resistor is used for?", "option_a": "Voltage rating", "option_b": "Resistance value", "option_c": "Current rating", "option_d": "Power rating", "correct_option": "B"},
    {"question": "Oscilloscope is used to measure?", "option_a": "Voltage over time", "option_b": "Current over time", "option_c": "Resistance", "option_d": "Capacitance", "correct_option": "A"},
    {"question": "Amplifier amplifies?", "option_a": "Voltage", "option_b": "Current", "option_c": "Power", "option_d": "All", "correct_option": "D"},
    {"question": "Diode allows current in?", "option_a": "One direction", "option_b": "Both directions", "option_c": "None", "option_d": "Variable", "correct_option": "A"},
    {"question": "Transistor has how many terminals?", "option_a": "2", "option_b": "3", "option_c": "4", "option_d": "5", "correct_option": "B"},
    {"question": "Logic '0' voltage level?", "option_a": "0V", "option_b": "5V", "option_c": "12V", "option_d": "3.3V", "correct_option": "A"},
    {"question": "Logic '1' voltage level in TTL?", "option_a": "0V", "option_b": "5V", "option_c": "3V", "option_d": "12V", "correct_option": "B"},
    {"question": "Multiplexer has how many data inputs for 1 output?", "option_a": "2^n", "option_b": "n", "option_c": "1", "option_d": "Depends", "correct_option": "A"},
    {"question": "De-multiplexer does?", "option_a": "One input to many outputs", "option_b": "Many inputs to one output", "option_c": "Logic operation", "option_d": "Amplification", "correct_option": "A"},
    {"question": "Which memory is volatile?", "option_a": "RAM", "option_b": "ROM", "option_c": "PROM", "option_d": "EPROM", "correct_option": "A"},
    {"question": "Which memory is non-volatile?", "option_a": "RAM", "option_b": "ROM", "option_c": "SRAM", "option_d": "DRAM", "correct_option": "B"},
    {"question": "Full form of VLSI?", "option_a": "Very Large Scale Integration", "option_b": "Very Low Scale Integration", "option_c": "Virtual Large Scale Integration", "option_d": "None", "correct_option": "A"},
    {"question": "Full form of FPGA?", "option_a": "Field Programmable Gate Array", "option_b": "Fast Programmable Gate Array", "option_c": "Full Programmable Gate Array", "option_d": "None", "correct_option": "A"},
    {"question": "LED emits?", "option_a": "Light", "option_b": "Heat", "option_c": "Current", "option_d": "Voltage", "correct_option": "A"},
    {"question": "Photodiode converts?", "option_a": "Light to electricity", "option_b": "Electricity to light", "option_c": "Current to voltage", "option_d": "Resistance to voltage", "correct_option": "A"}
]

with app.app_context():
    for q in ece_questions:
        existing = Question.query.filter_by(question=q["question"]).first()
        if not existing:  # prevent duplicates
            question = Question(
                department="ECE",
                question=q["question"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"]
            )
            db.session.add(question)
    db.session.commit()
    print("✅ All 50 ECE Questions Added Successfully!")
