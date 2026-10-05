import { useState } from "react";
import AnswerCard from "./components/AnswerCard.jsx";
import Header from "./components/Header.jsx";
import LoadingIndicator from "./components/LoadingIndicator.jsx";
import QuestionForm from "./components/QuestionForm.jsx";
import SourceCard from "./components/SourceCard.jsx";
import { askAssistant } from "./services/assistantApi.js";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askQuestion = async (event) => {
    event.preventDefault();

    if (!question.trim()) {
      setError("Please enter a question.");
      return;
    }

    setLoading(true);
    setError("");
    setAnswer("");
    setSources([]);

    try {
      const data = await askAssistant(question);
      setAnswer(data.answer);
      setSources(data.sources ?? []);
    } catch {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <Header />

      <main className="main-content">
        <section className="intro" aria-labelledby="page-title">
          <p className="eyebrow">COMPANY KNOWLEDGE, MADE ACCESSIBLE</p>
          <h1 id="page-title">Ask with confidence.</h1>
          <p className="intro-description">
            Get clear answers about company policies, backed by the documents
            they come from.
          </p>
        </section>

        <section className="assistant-panel" aria-label="Ask a policy question">
          <QuestionForm
            question={question}
            onQuestionChange={setQuestion}
            onSubmit={askQuestion}
            loading={loading}
          />

          {error && (
            <p className="error-message" role="alert">
              <span className="error-icon" aria-hidden="true">
                !
              </span>
              {error}
            </p>
          )}
        </section>

        {loading && <LoadingIndicator />}

        {answer && (
          <section className="results" aria-label="Answer and references">
            <AnswerCard answer={answer} />

            {sources.length > 0 && (
              <section className="sources-section" aria-labelledby="sources-title">
                <div className="section-heading">
                  <div>
                    <p className="eyebrow">BACKED BY DOCUMENTS</p>
                    <h2 id="sources-title">Sources</h2>
                  </div>
                  <span className="source-count">
                    {sources.length} {sources.length === 1 ? "source" : "sources"}
                  </span>
                </div>
                <div className="source-list">
                  {sources.map((source, index) => (
                    <SourceCard
                      key={`${source.title}-${source.page}-${index}`}
                      source={source}
                    />
                  ))}
                </div>
              </section>
            )}
          </section>
        )}

        <footer className="page-footer">
          <span className="footer-mark" aria-hidden="true">
            i
          </span>
          Answers are generated from your organization&apos;s trusted documents.
        </footer>
      </main>
    </div>
  );
}

export default App;
