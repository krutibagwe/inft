import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Restaurant App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange),
        useMaterial3: true,
       
      ),
      home: const RestaurantHomePage(),
    );
  }
}

class RestaurantHomePage extends StatelessWidget {
  const RestaurantHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Welcome to Foodie's Hub"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.network(
            "https://t3.ftcdn.net/jpg/03/24/73/92/360_F_324739203_keeq8udvv0P2h1MLYJ0GLSlTBagoXS48.jpg"
         
          ),
          const SizedBox(height: 20),
          const Text(
            'Foodie’s Hub Restaurant',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const MenuPage()),
          );
        },
        child: const Icon(Icons.restaurant_menu),
      ),
    );
  }
}

class MenuPage extends StatelessWidget {
  const MenuPage({super.key});

  @override
  Widget build(BuildContext context) {
    List<Map<String, String>> foodItems = [
      {
        'name': 'Pizza',
        'price': '₹250',
        'image':
            'https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_960_720.jpg'
      },
      {
        'name': 'Burger',
        'price': '₹150',
        'image':
            'https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_960_720.jpg'
      },
      {
        'name': 'Pasta',
        'price': '₹180',
        'image':
            'https://www.sharmispassions.com/wp-content/uploads/2015/12/alfredopasta5-500x500.jpg'
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text("Menu"),
        automaticallyImplyLeading: true,
      ),
      body: ListView.builder(
        itemCount: foodItems.length,
        itemBuilder: (context, index) {
          final item = foodItems[index];
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
