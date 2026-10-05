import ReactMarkdown from "react-markdown";

function AnswerCard({ answer }) {
  return (
    <article className="answer-card" aria-labelledby="answer-title">
      <div className="answer-heading">
        <span className="answer-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none">
            <path
              d="M12 3.75 14.2 9.8l6.05 2.2-6.05 2.2L12 20.25 9.8 14.2l-6.05-2.2 6.05-2.2L12 3.75Z"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinejoin="round"
            />
          </svg>
        </span>
        <div>
          <p className="eyebrow">YOUR ANSWER</p>
          <h2 id="answer-title">Here&apos;s what I found</h2>
        </div>
      </div>
      <div className="answer-text">
        <ReactMarkdown>
          {answer}
        </ReactMarkdown>
      </div>
    </article>
  );
}

export default AnswerCard;
