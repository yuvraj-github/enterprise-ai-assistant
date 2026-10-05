function LoadingIndicator() {
  return (
    <div className="loading-indicator" role="status" aria-live="polite">
      <span className="loading-spinner" aria-hidden="true" />
      <div>
        <p className="loading-title">Finding the right answer</p>
        <p className="loading-description">
          Searching trusted company documents…
        </p>
      </div>
    </div>
  );
}

export default LoadingIndicator;
