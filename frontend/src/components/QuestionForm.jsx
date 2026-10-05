function QuestionForm({ question, onQuestionChange, onSubmit, loading }) {
  return (
    <form className="question-form" onSubmit={onSubmit}>
      <label className="question-label" htmlFor="question">
        What would you like to know?
      </label>
      <textarea
        id="question"
        name="question"
        className="question-input"
        placeholder="e.g. How many vacation days do employees get?"
        rows={3}
        value={question}
        onChange={(event) => onQuestionChange(event.target.value)}
        aria-required="true"
        aria-describedby="question-hint"
      />
      <div className="form-footer">
        <p className="input-hint" id="question-hint">
          Ask about policies, benefits, and company guidelines.
        </p>
        <button className="ask-button" type="submit" disabled={loading}>
          {loading ? (
            <>
              <span className="button-spinner" aria-hidden="true" />
              Asking…
            </>
          ) : (
            <>
              Ask AI
              <svg viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <path
                  d="M4 10h12m-5-5 5 5-5 5"
                  stroke="currentColor"
                  strokeWidth="1.7"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </>
          )}
        </button>
      </div>
    </form>
  );
}

export default QuestionForm;
