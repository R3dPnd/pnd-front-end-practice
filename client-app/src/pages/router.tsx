import { createBrowserRouter } from "react-router";
import Home from "./home/home";
import ChessBoard from "../componenets/chess-board/chess-board";
import CompPractice from "./comp-practice/comp-practice";
import TicTacToe from "../componenets/tic-tac-toe/tic-tac-toe";

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
  },
  {
    path: "/tic-tac-toe",
    element: <TicTacToe/>
  }
]

export const router = createBrowserRouter(routes);