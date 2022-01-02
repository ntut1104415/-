import streamlit as st
import numpy as np


# From: https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def checkRows(board): #檢查行
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None

def checkcolumns(board): #檢查列
    for columns in board:
        if len(set(columns)) == 1:
            return columns[0]
    return None


def checkDiagonals(board):#檢查對角線
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return None


def checkWin(board): #檢查勝利
    # transposition to check rows, then columns檢查行列
    for newBoard in [board, np.transpose(board)]:
        result1 = checkRows(newBoard)
        if result1:
            return result2  
        result2 = checkRows(newBoard)
        if result2:
            return result1
    return checkDiagonals(board)


def show():
    st.write(
        """
        ## 🎮 Tic Tac Toe
        
        Let's play! This demo stores the entire game state (as a dict) in 
        `st.session_state` and uses the new callbacks to handle button clicks.
        """
    )
    st.write("")

    # Initialize state.初始化狀態。
    if "board" not in st.session_state:
        st.session_state.board = np.full((5, 5), "*", dtype=str)
        st.session_state.next_player = "🐶"
        st.session_state.winner = None

    # Define callbacks to handle button clicks.定義回調來處理按鈕點擊。
    def handle_click(i, j):
        if not st.session_state.winner:
            # TODO: Handle the case when nobody wins but the game is over!TODO：處理沒有人贏但遊戲結束的情況！
            st.session_state.board[i, j] = st.session_state.next_player
            st.session_state.next_player = (
                "🐱" if st.session_state.next_player == "🐶" else "🐶"
            )
            winner = checkWin(st.session_state.board)
            if winner != "*":
                st.session_state.winner = winner

    # Show one button for each field.為每個字段顯示一個按鈕。
    for i, row in enumerate(st.session_state.board):
        cols = st.columns([0.1, 0.1, 0.1, 0.1, 0.1])
        for j, field in enumerate(row):
            cols[j].button(
                field,
                key=f"{i}-{j}",
                on_click=handle_click,
                args=(i, j),
            )

    if st.session_state.winner:
        st.success(f"🏆Congrats! {st.session_state.winner} won the game! 🏆")


if __name__ == "__main__":
    show()
