import React from 'react';
import { createRoot } from "react-dom/client";import './index.css';
import { BrowserRouter, Routes, Route, createBrowserRouter, RouterProvider, Link } from "react-router-dom";
import Home from "./pages/Home";
import Stats from "./pages/Stats";
import './App.css';
import App from "./App"
import Redirect from "./pages/Redirect"
import Root from "./components/Root"


const router = createBrowserRouter(

  [{
    path: "/",
    element: <Root />,
  },
    {
      path: "home",
      element: <Home />,
    },
    {
      path: "overview",
      element: <Stats />,
    },
    {
      path: "redirect/:token",
      element: <Redirect />,
    },

  ]

);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
