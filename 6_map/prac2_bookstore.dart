import 'package:flutter/material.dart';

void main() {
  runApp(const BookStoreApp());
}

class BookStoreApp extends StatelessWidget {
  const BookStoreApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Book Store',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueAccent),
        useMaterial3: true,
      ),
      home: const BookStoreHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class BookStoreHomePage extends StatelessWidget {
  const BookStoreHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("The Book Haven"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.network(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW_SQK2eJgvMn0oK1iMpwE3eHkyMijQmT0DQ&s",
            height: 200,
          ),
          const SizedBox(height: 20),
          const Text(
            "The Book Haven",
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const BookMenuPage()),
          );
        },
        child: const Icon(Icons.menu_book),
      ),
    );
  }
}

class BookMenuPage extends StatelessWidget {
  const BookMenuPage({super.key});

  @override
  Widget build(BuildContext context) {
    List<Map<String, String>> books = [
      {
        'name': 'Atomic Habits',
        'price': '₹399',
        'image':
            'https://m.media-amazon.com/images/I/91bYsX41DVL._SY466_.jpg'
      },
      {
        'name': 'The Alchemist',
        'price': '₹299',
        'image':
            'https://m.media-amazon.com/images/I/71aFt4+OTOL._SY466_.jpg'
      },
      {
        'name': 'Think and Grow Rich',
        'price': '₹150',
        'image':
            'https://m.media-amazon.com/images/I/81h2gWPTYJL._SY466_.jpg'
      },
      {
        'name': 'Rich Dad Poor Dad',
        'price': '₹220',
        'image':
            'https://m.media-amazon.com/images/I/81bsw6fnUiL._SY466_.jpg'
      },
      {
        'name': 'Ikigai',
        'price': '₹270',
        'image':
            'https://m.media-amazon.com/images/I/71tbalAHYCL._SY466_.jpg'
      },
      {
        'name': 'Wings of Fire',
        'price': '₹180',
        'image':
            'https://m.media-amazon.com/images/I/71V46+-55yL._AC_UF1000,1000_QL80_.jpg'
      },
      {
        'name': 'The Psychology of Money',
        'price': '₹360',
        'image':
            'https://m.media-amazon.com/images/I/71g2ednj0JL._SY466_.jpg'
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text("Available Books"),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: ListView.builder(
        itemCount: books.length,
        itemBuilder: (context, index) {
          final item = books[index];
          return Card(
            margin: const EdgeInsets.all(10),
            child: ListTile(
              leading: Image.network(item['image']!, width: 50),
              title: Text(item['name']!),
              subtitle: Text("Price: ${item['price']}"),
            ),
          );
        },
      ),
    );
  }
}
