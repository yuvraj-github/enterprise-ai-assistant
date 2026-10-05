function Header() {
  return (
    <header className="app-header">
      <a className="brand" href="/" aria-label="Enterprise AI Assistant home">
        <span className="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none">
            <path
              d="M12 3.5 19.5 7.75v8.5L12 20.5l-7.5-4.25v-8.5L12 3.5Z"
              stroke="currentColor"
              strokeWidth="1.6"
              strokeLinejoin="round"
            />
            <path
              d="M8.5 12h7M12 8.5v7"
              stroke="currentColor"
              strokeWidth="1.6"
              strokeLinecap="round"
            />
          </svg>
        </span>
        <span className="brand-name">Northstar</span>
        <span className="brand-divider" aria-hidden="true" />
        <span className="brand-product">AI Assistant</span>
      </a>
      <span className="header-status">
        <span className="status-dot" aria-hidden="true" />
        Knowledge assistant
      </span>
    </header>
  );
}

export default Header;
