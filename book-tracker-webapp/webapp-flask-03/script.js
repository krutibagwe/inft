let books = [];

function addBook() {
    const title = document.getElementById("book-title").value;
    const author = document.getElementById("book-author").value;
    const totalPages = parseInt(document.getElementById("total-pages").value);
    const pagesRead = parseInt(document.getElementById("pages-read").value);

    const existingBook = books.find(book => book.title === title);

    if (existingBook) {
        existingBook.pagesRead = pagesRead;

        if (existingBook.pagesRead === existingBook.totalPages) {
            existingBook.status = "completed";
        }
    } else {
        const book = { title, author, totalPages, pagesRead, status: "in-progress", favorite: false };
        books.push(book);
    }

    updateBookList();
    saveBooksToLocalStorage();
    document.getElementById("book-form").reset();
}

function updateBookList() {
    const bookListDiv = document.getElementById("book-list");
    const completedBookListDiv = document.getElementById("completed-book-list");
    const favoriteBookListDiv = document.getElementById("favorite-book-list");

    bookListDiv.innerHTML = "";
    completedBookListDiv.innerHTML = "";
    favoriteBookListDiv.innerHTML = "";

    books.forEach((book, index) => {
        const progress = (book.pagesRead / book.totalPages) * 100;
        const progressBarClass = book.status === "completed" ? "completed-bar" : "in-progress-bar";
        const progressBar = `<div class="progress-bar ${progressBarClass}" style="width:${progress}%;"></div>`;
        const bookItem = `
            <div class="book-item">
                <h2>${book.title}</h2>
                <p>${book.author}</p>
                <p>${book.pagesRead} / ${book.totalPages} pages</p>
                <div class="progress">${progressBar}</div>
                <button onclick="toggleFavorite(${index})">${book.favorite ? 'Unmark Favorite' : 'Mark Favorite'}</button>
            </div>
        `;

        if (book.status === "completed") {
            completedBookListDiv.innerHTML += bookItem;
        } else {
            bookListDiv.innerHTML += bookItem;
        }

        if (book.favorite) {
            favoriteBookListDiv.innerHTML += bookItem;
        }
    });
}

function toggleFavorite(index) {
    books[index].favorite = !books[index].favorite;
    updateBookList();
    saveBooksToLocalStorage();
}

function clearProgress() {
    books = [];
    updateBookList();
    saveBooksToLocalStorage();
}

function saveBooksToLocalStorage() {
    localStorage.setItem("books", JSON.stringify(books));
}

function loadBooksFromLocalStorage() {
    const storedBooks = localStorage.getItem("books");
    if (storedBooks) {
        books = JSON.parse(storedBooks);
        updateBookList();
    }
}

window.onload = loadBooksFromLocalStorage;
