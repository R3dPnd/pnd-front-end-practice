import { createBrowserRouter } from "react-router";
import Home from "./home/home";
import ChessBoard from "../componenets/chess-board/chess-board";
import CompPractice from "./comp-practice/comp-practice";

const routes = [
  {
    path: "/",
    element: <Home/>
  },
  {
    path: "/chess-board",
    element: <ChessBoard/>
  },
  {
    path: "/practice",
    element: <CompPractice/>
  }
]

export const router = createBrowserRouter(routes);