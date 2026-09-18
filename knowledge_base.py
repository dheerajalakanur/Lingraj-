import random

KNOWLEDGE_BASE = [
    {
        "conditions": ["low rainfall", "low soil organic carbon", "semi-arid", "monoculture"],
        "recommendation": {
            "en": "Introduce legume-based cover crops and agroforestry (e.g., intercropping with drought-resistant trees).",
            "hi": "फलीदार आवरण फसलें और कृषि वानिकी (जैसे, सूखे-प्रतिरोधी पेड़ों के साथ अंतर-फसल) शुरू करें।",
            "kn": "ದ್ವಿದಳ ಧಾನ್ಯ ಆಧಾರಿತ ಬೆಳೆಗಳು ಮತ್ತು ಕೃಷಿ ಅರಣ್ಯವನ್ನು ಪರಿಚಯಿಸಿ (ಉದಾ: ಬರ-ನಿರೋಧಕ ಮರಗಳೊಂದಿಗೆ ಅಂತರಬೆಳೆ)."
        },
        "scientific_reasoning": {
            "en": "Legumes fix nitrogen and increase soil organic carbon by ~15-25% over 2-3 years. Agroforestry provides shade, reducing moisture loss, and creates habitat for diverse species, improving microbial diversity and pollinator support.",
            "hi": "फलियां नाइट्रोजन को ठीक करती हैं और 2-3 वर्षों में मिट्टी में कार्बनिक कार्बन को 15-25% तक बढ़ाती हैं। कृषि वानिकी छाया प्रदान करती है, जिससे नमी की कमी कम होती है, और यह विविध प्रजातियों के लिए आवास बनाती है।",
            "kn": "ದ್ವಿದಳ ಧಾನ್ಯಗಳು ಸಾರಜನಕವನ್ನು ಸ್ಥಿರಗೊಳಿಸುತ್ತವೆ ಮತ್ತು 2-3 ವರ್ಷಗಳಲ್ಲಿ ಮಣ್ಣಿನ ಸಾವಯವ ಇಂಗಾಲವನ್ನು 15-25% ರಷ್ಟು ಹೆಚ್ಚಿಸುತ್ತವೆ. ಕೃಷಿ ಅರಣ್ಯವು ನೆರಳು ನೀಡುತ್ತದೆ ಮತ್ತು ತೇವಾಂಶದ ನಷ್ಟವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ."
        },
        "impacted_metrics": {
            "en": ["Soil Health (Organic Carbon)", "Biodiversity (Species Richness)", "Water Availability (Moisture Retention)"],
            "hi": ["मिट्टी का स्वास्थ्य (जैविक कार्बन)", "जैव विविधता (प्रजातियों की समृद्धि)", "पानी की उपलब्धता (नमी प्रतिधारण)"],
            "kn": ["ಮಣ್ಣಿನ ಆರೋಗ್ಯ (ಸಾವಯವ ಇಂಗಾಲ)", "ಜೀವವೈವಿಧ್ಯ (ಜಾತಿಗಳ ಶ್ರೀಮಂತಿಕೆ)", "ನೀರಿನ ಲಭ್ಯತೆ (ತೇವಾಂಶ ಧಾರಣೆ)"]
        },
        "time_horizon": {
            "en": "Medium-term (2-3 years)",
            "hi": "मध्यम अवधि (2-3 वर्ष)",
            "kn": "ಮಧ್ಯಮ ಅವಧಿ (2-3 ವರ್ಷಗಳು)"
        },
        "confidence": {
            "en": "92%",
            "hi": "92%",
            "kn": "92%"
        },
        "reference": {
            "en": "Food and Agriculture Organization (FAO) studies on agroforestry; Intergovernmental Panel on Climate Change (IPCC) on semi-arid soils.",
            "hi": "कृषि वानिकी पर खाद्य एवं कृषि संगठन (FAO) के अध्ययन; अर्ध-शुष्क मिट्टी पर जलवायु परिवर्तन पर अंतर सरकारी पैनल (IPCC)।",
            "kn": "ಕೃಷಿ ಅರಣ್ಯದ ಕುರಿತು ಆಹಾರ ಮತ್ತು ಕೃಷಿ ಸಂಸ್ಥೆ (FAO) ಅಧ್ಯಯನಗಳು; ಅರೆ-ಶುಷ್ಕ ಮಣ್ಣಿನ ಬಗ್ಗೆ ಹವಾಮಾನ ಬದಲಾವಣೆಯ ಅಂತರಸರ್ಕಾರಿ ಸಮಿತಿ (IPCC)."
        }
    },
    {
        "conditions": ["high pollution", "habitat fragmentation", "urban"],
        "recommendation": {
            "en": "Establish green corridors with native plant species and implement bioretention swales.",
            "hi": "देशी पौधों की प्रजातियों के साथ हरित गलियारे स्थापित करें और बायोरिटेंशन स्वेल लागू करें।",
            "kn": "ಸ್ಥಳೀಯ ಸಸ್ಯ ಪ್ರಭೇದಗಳೊಂದಿಗೆ ಹಸಿರು ಕಾರಿಡಾರ್‌ಗಳನ್ನು ಸ್ಥಾಪಿಸಿ ಮತ್ತು ಜೈವಿಕ ಧಾರಣ ಸ್ವಾಲೆಗಳನ್ನು ಅಳವಡಿಸಿ."
        },
        "scientific_reasoning": {
            "en": "Green corridors connect fragmented habitats, allowing species migration. Bioretention swales filter urban runoff pollutants before they reach local waterways, directly improving water quality and supporting aquatic biodiversity.",
            "hi": "हरित गलियारे खंडित आवासों को जोड़ते हैं, जिससे प्रजातियों का प्रवास होता है। बायोरिटेंशन स्वेल स्थानीय जलमार्गों तक पहुंचने से पहले शहरी अपवाह प्रदूषकों को फ़िल्टर करते हैं।",
            "kn": "ಹಸಿರು ಕಾರಿಡಾರ್‌ಗಳು ಛಿದ್ರಗೊಂಡ ಆವಾಸಸ್ಥಾನಗಳನ್ನು ಸಂಪರ್ಕಿಸುತ್ತವೆ, ಪ್ರಭೇದಗಳ ವಲಸೆಗೆ ಅವಕಾಶ ಮಾಡಿಕೊಡುತ್ತವೆ. ಜೈವಿಕ ಧಾರಣ ಸ್ವಾಲೆಗಳು ನೀರಿನ ಗುಣಮಟ್ಟವನ್ನು ಸುಧಾರಿಸುತ್ತವೆ."
        },
        "impacted_metrics": {
            "en": ["Habitat Diversity", "Water Quality", "Pollution Reduction"],
            "hi": ["आवास विविधता", "पानी की गुणवत्ता", "प्रदूषण में कमी"],
            "kn": ["ಆವಾಸಸ್ಥಾನ ವೈವಿಧ್ಯ", "ನೀರಿನ ಗುಣಮಟ್ಟ", "ಮಾಲಿನ್ಯ ಕಡಿತ"]
        },
        "time_horizon": {
            "en": "Long-term (5-10 years)",
            "hi": "दीर्घकालिक (5-10 वर्ष)",
            "kn": "ದೀರ್ಘಕಾಲೀನ (5-10 ವರ್ಷಗಳು)"
        },
        "confidence": {
            "en": "88%",
            "hi": "88%",
            "kn": "88%"
        },
        "reference": {
            "en": "Urban Ecology research on green infrastructure (EPA).",
            "hi": "हरित बुनियादी ढांचे पर शहरी पारिस्थितिकी अनुसंधान (EPA)।",
            "kn": "ಹಸಿರು ಮೂಲಸೌಕರ್ಯ ಕುರಿತು ನಗರ ಪರಿಸರ ವಿಜ್ಞಾನ ಸಂಶೋಧನೆ (EPA)."
        }
    },
    {
        "conditions": ["low soil moisture", "high temperature", "deforestation"],
        "recommendation": {
            "en": "Implement holistic planned grazing and reforestation with pioneer species.",
            "hi": "समग्र नियोजित चराई और अग्रणी प्रजातियों के साथ पुनर्वनीकरण लागू करें।",
            "kn": "ಸಮಗ್ರ ಯೋಜಿತ ಮೇಯಿಸುವಿಕೆ ಮತ್ತು ಪ್ರವರ್ತಕ ಜಾತಿಗಳೊಂದಿಗೆ ಅರಣ್ಯೀಕರಣವನ್ನು ಜಾರಿಗೊಳಿಸಿ."
        },
        "scientific_reasoning": {
            "en": "Holistic grazing breaks up capped soil, allowing water infiltration. Pioneer species provide rapid ground cover, lowering local soil temperatures through shading and evaporative cooling, which aids in ecosystem recovery.",
            "hi": "समग्र चराई से मिट्टी टूटती है, जिससे पानी का प्रवेश होता है। अग्रणी प्रजातियां तेजी से जमीन को ढंकती हैं, जिससे छाया और वाष्पीकरणीय शीतलन के माध्यम से मिट्टी का तापमान कम होता है।",
            "kn": "ಸಮಗ್ರ ಮೇಯಿಸುವಿಕೆಯು ಮುಚ್ಚಿದ ಮಣ್ಣನ್ನು ಒಡೆಯುತ್ತದೆ, ನೀರಿನ ಒಳನುಗ್ಗುವಿಕೆಗೆ ಅವಕಾಶ ಮಾಡಿಕೊಡುತ್ತದೆ. ಪ್ರವರ್ತಕ ಜಾತಿಗಳು ವೇಗವಾಗಿ ನೆಲದ ಹೊದಿಕೆಯನ್ನು ಒದಗಿಸುತ್ತವೆ."
        },
        "impacted_metrics": {
            "en": ["Soil Health (Moisture)", "Climate Factors (Local Temperature)", "Biodiversity (Flora)"],
            "hi": ["मिट्टी का स्वास्थ्य (नमी)", "जलवायु कारक (स्थानीय तापमान)", "जैव विविधता (वनस्पति)"],
            "kn": ["ಮಣ್ಣಿನ ಆರೋಗ್ಯ (ತೇವಾಂಶ)", "ಹವಾಮಾನ ಅಂಶಗಳು (ಸ್ಥಳೀಯ ತಾಪಮಾನ)", "ಜೀವವೈವಿಧ್ಯ (ಸಸ್ಯವರ್ಗ)"]
        },
        "time_horizon": {
            "en": "Short to Medium-term (1-5 years)",
            "hi": "लघु से मध्यम अवधि (1-5 वर्ष)",
            "kn": "ಅಲ್ಪದಿಂದ ಮಧ್ಯಮ ಅವಧಿ (1-5 ವರ್ಷಗಳು)"
        },
        "confidence": {
            "en": "85%",
            "hi": "85%",
            "kn": "85%"
        },
        "reference": {
            "en": "Savory Institute on holistic management; UN Environment Programme on reforestation.",
            "hi": "समग्र प्रबंधन पर सेवरी संस्थान; पुनर्वनीकरण पर संयुक्त राष्ट्र पर्यावरण कार्यक्रम।",
            "kn": "ಸಮಗ್ರ ನಿರ್ವಹಣೆಯ ಕುರಿತು ಸೇವರಿ ಇನ್ಸ್ಟಿಟ್ಯೂಟ್; ಅರಣ್ಯೀಕರಣದ ಕುರಿತು ಯುಎನ್ ಪರಿಸರ ಕಾರ್ಯಕ್ರಮ."
        }
    }
]

def retrieve_knowledge(user_input: str, structured_data: dict = None):
    input_text = user_input.lower()
    
    best_match = None
    max_matches = 0
    
    for entry in KNOWLEDGE_BASE:
        matches = sum(1 for condition in entry["conditions"] if condition in input_text)
        if structured_data:
            for key, val in structured_data.items():
                if isinstance(val, str) and val.lower() in entry["conditions"]:
                    matches += 1

        if matches > max_matches:
            max_matches = matches
            best_match = entry
            
    if best_match:
        return best_match
    else:
        return random.choice(KNOWLEDGE_BASE)
