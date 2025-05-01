import 'package:flutter/material.dart';

void main() {
  runApp(const MobileStoreApp());
}

class MobileStoreApp extends StatelessWidget {
  const MobileStoreApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mobile Store',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
        useMaterial3: true,
      ),
      home: const MobileStoreHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MobileStoreHomePage extends StatelessWidget {
  const MobileStoreHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Mobile Store"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Image.network(
            "https://media.istockphoto.com/id/1366731738/photo/shopping-a-new-digital-device-happy-couple-buying-a-smartphone-in-store.jpg?s=612x612&w=0&k=20&c=QCNGucAdNwLTz9YkRFuCSnturfRsUfk_nKwjtlQg6B4=",
            height: 200,
          ),
          const SizedBox(height: 20),
          const Text(
            "Welcome to Mobile Store",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const MobileMenuPage()),
          );
        },
        child: const Icon(Icons.phone_android),
      ),
    );
  }
}

class MobileMenuPage extends StatelessWidget {
  const MobileMenuPage({super.key});

  @override
  Widget build(BuildContext context) {
    List<Map<String, String>> mobiles = [
      {
    'name': 'Samsung Galaxy A14',
    'price': '₹14,000',
    'image': 'https://m.media-amazon.com/images/I/814ePfNubRL._SX679_.jpg'
  },
  {
    'name': 'Redmi Note 12',
    'price': '₹17,000',
    'image': 'https://m.media-amazon.com/images/I/61VbKHdE0rL._SX679_.jpg'
  },
  {
    'name': 'Realme Narzo 50',
    'price': '₹12,500',
    'image': 'https://m.media-amazon.com/images/I/81ewGd2-9eL._SX679_.jpg'
  },
  {
    'name': 'Poco M4 Pro',
    'price': '₹13,500',
    'image': 'https://m.media-amazon.com/images/I/71dEY4Neo3L._SX679_.jpg'
  },
  {
    'name': 'iQOO Z6',
    'price': '₹15,999',
    'image': 'https://m.media-amazon.com/images/I/61JS7lF2aqL._SX679_.jpg'
  },
  {
    'name': 'Vivo Y16',
    'price': '₹11,000',
    'image': 'https://m.media-amazon.com/images/I/61g1v5mjsyL._SX679_.jpg'
  },
  {
    'name': 'Motorola G31',
    'price': '₹10,499',
    'image': 'https://m.media-amazon.com/images/I/61exfL8UwnL._SX679_.jpg'
  },
];
    return Scaffold(
      appBar: AppBar(
        title: const Text("Available Mobiles"),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: ListView.builder(
        itemCount: mobiles.length,
        itemBuilder: (context, index) {
          final item = mobiles[index];
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
