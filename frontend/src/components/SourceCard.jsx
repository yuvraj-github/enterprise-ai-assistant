function SourceCard({ source }) {
  return (
    <article className="source-card">
      <span className="document-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none">
          <path
            d="M7 3.75h7l4 4v12.5H7a2 2 0 0 1-2-2V5.75a2 2 0 0 1 2-2Z"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinejoin="round"
          />
          <path
            d="M14 3.75v4h4M8.5 12h7m-7 3.5h7"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
        </svg>
      </span>
      <div className="source-details">
        <h3>{source.title}</h3>
        <div className="source-metadata">
          <span>Page {source.page}</span>
          <span className="metadata-divider" aria-hidden="true" />
          <span>{source.department}</span>
        </div>
      </div>
      <span className="source-reference" aria-hidden="true">
        ↗
      </span>
    </article>
  );
}

export default SourceCard;
