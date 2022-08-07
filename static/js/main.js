document.addEventListener("DOMContentLoaded", () => {
    createSquares();

    let guessedWords = [[]];
    let availableSpace = 1;

    let word;
    let guessedWordCount = 0;

    let gamecontinue = true
    getNewWord();

    document.addEventListener('keydown', (e) => {
      if (gamecontinue) {
        const key = e.key.toLowerCase();
        if (e.code.startsWith("Key")) {
              updateGuessedWords(key);
        }
        if (key === "enter") {
              handleSubmitWord();
        }
        if (key === "delete" || key === "backspace") {
              handleDeleteLetter();
        }
      }
    });

    function getNewWord() {
        word = document.getElementById("generatedWord").textContent;
        console.log(word);
    }

    function getCurrentWordArr() {
        const numberOfGuessedWords = guessedWords.length;
        return guessedWords[numberOfGuessedWords - 1];
    }

    function updateGuessedWords(letter) {
        const currentWordArr = getCurrentWordArr();

        if (currentWordArr && currentWordArr.length < 5) {
            currentWordArr.push(letter);

            const availableSpaceEl = document.getElementById(String(availableSpace));

            availableSpace = availableSpace + 1;
            availableSpaceEl.textContent = letter;
        }
    }

    function getTileColor(letter, index) {
        const isCorrectLetter = word.includes(letter);

        if (!isCorrectLetter) {
            return "rgb(58, 58, 60)";
        }

        const letterInThatPosition = word.charAt(index);
        const isCorrectPosition = letter === letterInThatPosition;

        if (isCorrectPosition) {
            return "rgb(83, 141, 78)";
        }

        return "rgb(181, 159, 59)";
    }

    function handleSubmitWord() {
        const currentWordArr = getCurrentWordArr();
        if (currentWordArr.length !== 5) {
            window.alert("Word must be 5 letters");
        } else {
            const currentWord = currentWordArr.join("");
            const firstLetterId = guessedWordCount * 5 + 1;
            const interval = 200;
            currentWordArr.forEach((letter, index) => {
                setTimeout(() => {
                    const tileColor = getTileColor(letter, index);

                    const letterId = firstLetterId + index;
                    const letterEl = document.getElementById(letterId);
                    letterEl.classList.add("animate__flipInX");
                    letterEl.style = `background-color:${tileColor};border-color:${tileColor}`;
                }, interval * index);
            });

            guessedWordCount += 1;

            if (currentWord === word) {
                window.alert("Congratulations!");
                gamecontinue = false;
            }

            if (guessedWords.length === 6) {
                window.alert(`Sorry, you have no more guesses! The word is ${word}.`);
            }

            guessedWords.push([]);
        }

    }

    function createSquares() {
        const gameBoard = document.getElementById("board");

        for (let index = 0; index < 30; index++) {
            let square = document.createElement("div");
            square.classList.add("square");
            square.classList.add("animate__animated");
            square.setAttribute("id", index + 1);
            gameBoard.appendChild(square);
        }
    }

    function handleDeleteLetter() {
        const currentWordArr = getCurrentWordArr();
        currentWordArr.pop();
        guessedWords[guessedWords.length - 1] = currentWordArr;

        const lastLetterEl = document.getElementById(String(availableSpace - 1));

        lastLetterEl.textContent = "";
        availableSpace = availableSpace - 1;
    }
});