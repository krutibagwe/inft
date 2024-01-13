const authors = [
    "Jane Austen",
    "William Shakespeare",
    "George Orwell",
    "F. Scott Fitzgerald",
    "J.K. Rowling",
    "Ernest Hemingway",
    "Mark Twain",
    "Agatha Christie",
    "J.R.R. Tolkien",
    "Harper Lee"
];

const authorList = document.getElementById("author-list");

function populateAuthorList() {
    authors.forEach(author => {
        const listItem = document.createElement("li");
        listItem.textContent = author;
       /* listItem.addEventListener("click", () => {
            alert(`You selected ${author} as your favorite author!`);
        });*/
        authorList.appendChild(listItem);
    });
}

populateAuthorList();
