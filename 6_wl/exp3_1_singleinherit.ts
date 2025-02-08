class Book {  
    Title: string;  
    Author: string;  
    YearPublished: number;  
    IsAvailable: boolean;  
    constructor(title: string, author: string, yearPublished: number, isAvailable: boolean) {  
        this.Title = title;  
        this.Author = author;  
        this.YearPublished = yearPublished;  
        this.IsAvailable = isAvailable;  
    }  
}  
class Novel extends Book {  
    Genre: string;  
    Price: number;  
    constructor(title: string, author: string, yearPublished: number, isAvailable: boolean, genre: string, price: number) {  
        super(title, author, yearPublished, isAvailable);  
        this.Genre = genre;  
        this.Price = price;  
    }  
    display(): void {  
        console.log("Title of the Novel: " + this.Title);  
        console.log("Author of the Novel: " + this.Author);  
        console.log("Year Published: " + this.YearPublished);  
        console.log("Is the Novel Available? " + this.IsAvailable);  
        console.log("Genre of the Novel: " + this.Genre);  
        console.log("Price of the Novel: " + this.Price);  
    }  
}  
let novelObj = new Novel("The Great Adventure", "R K Laxman", 2023, true, "Adventure", 599);  
novelObj.display();
