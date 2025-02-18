import { createRoot } from "react-dom/client";
import { StrictMode } from "react";
import App from "./App";
import './App.css';

const root = createRoot(document.getElementById("root"));

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
