import { useState } from 'react';
import './tic-tac-toe.css';

export default function TicTacToe() {

    const [message, setMessage] = useState<string>("Welcome!")
    const [board, setBoard] = useState<string[][]>(Array(3).fill(null).map(() => Array(3).fill(null)))
    const [currentPlayer, setCurrentPlayer] = useState<string>("X")
    const [error, setError] = useState<string>("")
    
    const displayBoard = () => {
        return (
            <div className="board">
                {board.map((row, rowIndex: number) => (
                    <div key={rowIndex} className="row">
                        {displayRow(row, rowIndex)}
                    </div>
                ))}
            </div>
        )
    }

    function handleCellClick(rowIndex: number, colIndex: number): void {
        const newBoard = board.map(row => [...row]);
        if(newBoard[rowIndex][colIndex] !== null) {
            setError("Cell already occupied")
            return
        }
        newBoard[rowIndex][colIndex] = currentPlayer;
        setBoard(newBoard);
        setCurrentPlayer(currentPlayer === "X" ? "O" : "X");
        checkWin()
    }

    const displayRow = (row: any, rowIndex: number) => {
        console.log(row, rowIndex)
        return (
            <div className="row">
                {row.map((cell: any, colIndex: number) => {
                    return <div className="cell" onClick={() => handleCellClick(rowIndex, colIndex)}>{cell}</div>
                })
                }
            </div>
        )
    }

    const checkWin = () => {
        
    }

    function resetGame(): void {
        setBoard(Array(3).fill(null).map(() => Array(3).fill(null)))
        setCurrentPlayer("X")
        setError("")
        setMessage("Welcome!")
    }

    return (
    <div className="container">
      <h1>{message}</h1>
      {displayBoard()}
      <p>{error}</p>
      <button onClick={() => resetGame()}>Reset</button>
    </div>
  );
}