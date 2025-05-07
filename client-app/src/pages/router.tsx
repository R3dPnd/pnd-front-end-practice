import { createBrowserRouter } from "react-router";
import Home from "./home/home";
import ChessBoard from "../componenets/chess-board/chess-board";

const routes = [
  {
    path: "/",
    element: <Home/>
  },
  {
    path: "/chess-board",
    element: <ChessBoard/>
  }
]

export const router = createBrowserRouter(routes);