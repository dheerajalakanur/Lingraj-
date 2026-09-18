const { useState, useRef, useEffect } = React;

const translations = {
    en: {
        title: "Darukaa.Earth",
        subtitle: "AI Biodiversity Intelligence Chatbot",
        welcome: "Hello! I am the Darukaa.Earth AI Environmental Scientist. Please describe your land or ecosystem, including any relevant factors like soil health, rainfall, or land use.",
        recommendation: "Recommendation",
        whatToDo: "What to do:",
        whyItWorks: "Why it works (Scientific Reasoning):",
        impactedMetrics: "Impacted Metrics:",
        timeHorizon: "Time Horizon:",
        confidenceLevel: "Confidence Level:",
        references: "References:",
        analyzing: "Analyzing environmental variables...",
        placeholder: "E.g., Biodiversity is declining on my land...",
        send: "Send",
        error: "Sorry, I could not connect to the backend server."
    },
    hi: {
        title: "दारुका.अर्थ (Darukaa.Earth)",
        subtitle: "एआई जैव विविधता खुफिया चैटबॉट",
        welcome: "नमस्ते! मैं दारुका.अर्थ एआई पर्यावरण वैज्ञानिक हूँ। कृपया अपनी भूमि या पारिस्थितिकी तंत्र का वर्णन करें, जिसमें मिट्टी का स्वास्थ्य, वर्षा, या भूमि उपयोग जैसे कारक शामिल हों।",
        recommendation: "सिफारिश (Recommendation)",
        whatToDo: "क्या करें:",
        whyItWorks: "यह क्यों काम करता है (वैज्ञानिक कारण):",
        impactedMetrics: "प्रभावित मेट्रिक्स:",
        timeHorizon: "समय सीमा (Time Horizon):",
        confidenceLevel: "विश्वास स्तर (Confidence Level):",
        references: "संदर्भ (References):",
        analyzing: "पर्यावरणीय चर का विश्लेषण किया जा रहा है...",
        placeholder: "उदाहरण के लिए: कम बारिश के कारण मेरी जमीन पर जैव विविधता घट रही है...",
        send: "भेजें (Send)",
        error: "क्षमा करें, मैं बैकएंड सर्वर से कनेक्ट नहीं हो सका।"
    },
    kn: {
        title: "ದಾರುಕಾ.ಅರ್ಥ್ (Darukaa.Earth)",
        subtitle: "ಎಐ ಜೀವವೈವಿಧ್ಯ ಗುಪ್ತಚರ ಚಾಟ್‌ಬಾಟ್",
        welcome: "ನಮಸ್ಕಾರ! ನಾನು ದಾರುಕಾ.ಅರ್ಥ್ ಎಐ ಪರಿಸರ ವಿಜ್ಞಾನಿ. ಮಣ್ಣಿನ ಆರೋಗ್ಯ, ಮಳೆ ಅಥವಾ ಭೂ ಬಳಕೆಯಂತಹ ಅಂಶಗಳನ್ನು ಒಳಗೊಂಡಂತೆ ದಯವಿಟ್ಟು ನಿಮ್ಮ ಭೂಮಿ ಅಥವಾ ಪರಿಸರ ವ್ಯವಸ್ಥೆಯನ್ನು ವಿವರಿಸಿ.",
        recommendation: "ಶಿಫಾರಸು (Recommendation)",
        whatToDo: "ಏನು ಮಾಡಬೇಕು:",
        whyItWorks: "ಇದು ಏಕೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ (ವೈಜ್ಞಾನಿಕ ಕಾರಣ):",
        impactedMetrics: "ಪರಿಣಾಮ ಬೀರಿದ ಮೆಟ್ರಿಕ್‌ಗಳು:",
        timeHorizon: "ಸಮಯದ ಮಿತಿ (Time Horizon):",
        confidenceLevel: "ವಿಶ್ವಾಸಾರ್ಹತೆಯ ಮಟ್ಟ (Confidence Level):",
        references: "ಉಲ್ಲೇಖಗಳು (References):",
        analyzing: "ಪರಿಸರ ಅಸ್ಥಿರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...",
        placeholder: "ಉದಾಹರಣೆಗೆ: ಕಡಿಮೆ ಮಳೆಯಿಂದಾಗಿ ನನ್ನ ಭೂಮಿಯಲ್ಲಿ ಜೀವವೈವಿಧ್ಯವು ಕ್ಷೀಣಿಸುತ್ತಿದೆ...",
        send: "ಕಳುಹಿಸಿ (Send)",
        error: "ಕ್ಷಮಿಸಿ, ಬ್ಯಾಕೆಂಡ್ ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ."
    }
};

function App() {
    const [lang, setLang] = useState("en");
    const [messages, setMessages] = useState([
        {
            sender: "bot",
            text: translations["en"].welcome
        }
    ]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);
    const messagesEndRef = useRef(null);

    const t = translations[lang];

    const handleLangChange = (e) => {
        const newLang = e.target.value;
        setLang(newLang);
        // Add a welcome message in the new language
        setMessages(prev => [...prev, {
            sender: "bot",
            text: translations[newLang].welcome
        }]);
    };

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userText = input.trim();
        setMessages(prev => [...prev, { sender: "user", text: userText }]);
        setInput("");
        setLoading(true);

        try {
            const apiUrl = window.location.hostname.includes("localhost") || window.location.hostname.includes("127.0.0.1") 
                ? "http://localhost:8000/chat" 
                : "/chat";
                
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ 
                    message: userText,
                    language: lang 
                })
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            
            setMessages(prev => [...prev, {
                sender: "bot",
                text: data.response,
                details: data
            }]);
        } catch (error) {
            console.error("Error communicating with backend:", error);
            setMessages(prev => [...prev, { 
                sender: "bot", 
                text: t.error 
            }]);
        } finally {
            setLoading(false);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSend();
        }
    };

    return (
        <div className="chat-container">
            <div className="chat-header">
                <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                    <div>
                        <h1>{t.title}</h1>
                        <p>{t.subtitle}</p>
                    </div>
                    <div>
                        <select 
                            value={lang} 
                            onChange={handleLangChange}
                            style={{padding: '5px', borderRadius: '5px', border: 'none'}}
                        >
                            <option value="en">English</option>
                            <option value="hi">हिन्दी (Hindi)</option>
                            <option value="kn">ಕನ್ನಡ (Kannada)</option>
                        </select>
                    </div>
                </div>
            </div>
            
            <div className="chat-messages">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <div>{msg.text}</div>
                        {msg.details && msg.details.recommendation && (
                            <div className="bot-card">
                                <h4>{t.recommendation}</h4>
                                <p><strong>{t.whatToDo}</strong> {msg.details.recommendation}</p>
                                <p><strong>{t.whyItWorks}</strong> {msg.details.scientific_reasoning}</p>
                                
                                <div>
                                    <strong>{t.impactedMetrics}</strong>
                                    <div style={{marginTop: '5px'}}>
                                        {msg.details.impacted_metrics.map((metric, i) => (
                                            <span key={i} className="badge">{metric}</span>
                                        ))}
                                    </div>
                                </div>
                                
                                <p><strong>{t.timeHorizon}</strong> {msg.details.time_horizon}</p>
                                <p><strong>{t.confidenceLevel}</strong> {msg.details.confidence}</p>
                                <p><strong>{t.references}</strong> <em>{msg.details.reference}</em></p>
                            </div>
                        )}
                    </div>
                ))}
                {loading && (
                    <div className="message bot">
                        <em>{t.analyzing}</em>
                    </div>
                )}
                <div ref={messagesEndRef} />
            </div>

            <div className="chat-input-area">
                <input 
                    type="text" 
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder={t.placeholder}
                    disabled={loading}
                />
                <button onClick={handleSend} disabled={loading || !input.trim()}>
                    {t.send}
                </button>
            </div>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
