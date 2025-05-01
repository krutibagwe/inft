import 'package:flutter/material.dart';


void main() => runApp(const CollegeWebsite());


class CollegeWebsite extends StatelessWidget {
  const CollegeWebsite({super.key});


  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'College Website',
      debugShowCheckedModeBanner: false,
      home: const HomePage(),
    );
  }
}


class HomePage extends StatelessWidget {
  const HomePage({super.key});


  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 5,
      child: Scaffold(
        appBar: AppBar(
          title: Row(
            children: [
              Image.network(
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWFvTad6gAX0GtUSqjXKmiQ9sJx9z1i5YY6g&s',
                height: 40,
              ),
              const SizedBox(width: 10),
              const Text('St. Francis Institute of Technology'),
            ],
          ),
          bottom: const TabBar(
            isScrollable: true,
            tabs: [
              Tab(text: 'About Us'),
              Tab(text: 'Academics'),
              Tab(text: 'Library'),
              Tab(text: 'Placements'),
              Tab(text: 'Admissions'),
            ],
          ),
        ),
        body: const TabBarView(
          children: [
            TabContent([
              'Established in 1999.',
              'Affiliated to University of Mumbai.',
              'Accredited by NAAC with A Grade.',
            ]),
            TabContent([
              'BE Programs - CSE, IT, EXTC.',
              'ME Programs available.',
              'Industry-aligned curriculum.',
            ]),
            TabContent([
              '30,000+ books.',
              'Digital Library access.',
              'IEEE and J-Gate subscriptions.',
            ]),
            TabContent([
              '90%+ placements yearly.',
              'Top recruiters: TCS, Infosys.',
              'Training & internships offered.',
            ]),
            TabContent([
              'Admissions open for 2025.',
              'Based on MHT-CET / JEE Main.',
              'Online application available.',
            ]),
          ],
        ),
        bottomNavigationBar: Container(
          color: Colors.yellow[100],
          padding: const EdgeInsets.all(12),
          child: const Text(
            '📢 Admissions Open for 2025!',
            style: TextStyle(fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}


class TabContent extends StatelessWidget {
  final List<String> points;
  const TabContent(this.points, {super.key});


  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(16),
      children: points.map((text) => Padding(
        padding: const EdgeInsets.symmetric(vertical: 4),
        child: Text('• $text'),
      )).toList(),
    );
  }
}
