
package hotel.management.system;

import java.awt.Color;
import javax.swing.*;
import java.awt.event.*; 
import java.awt.*;


public class HotelManagementSystem extends JFrame implements ActionListener{
    
    HotelManagementSystem(){
        super("StayInnSight");
        setSize(1200, 600);
        setLocation(150,100);
        
        ImageIcon i1= new ImageIcon(ClassLoader.getSystemResource("images/hotel01.jpg"));
        Image i2= i1.getImage().getScaledInstance(1200, 600, Image.SCALE_DEFAULT);
        ImageIcon i3= new ImageIcon(i2);
       
        
        
        JLabel image= new JLabel(i3);
        image.setBounds(0, 0, 1200, 600);
        add(image);
        
                
        JLabel text= new JLabel("StayInnSight");
        text.setBounds(735,10,700,70);
        text.setForeground(Color.WHITE);
        text.setFont(new Font("Times New Roman", Font.PLAIN,45 ));
        add(text);
      
        image.add(text);
        
        JLabel text1= new JLabel("Manage hotels efficiently");
        text1.setBounds(720,70,700,40);
        text1.setForeground(Color.WHITE);
        text1.setFont(new Font("Times New Roman", Font.ITALIC,25 ));
        add(text1);
      
        image.add(text1);
         
        JButton next= new JButton("Next");
        next.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        next.setBounds(850, 450, 150, 40);
        next.setBackground(Color.WHITE);
        next.setForeground(Color.BLACK);
        image.add(next);
       next.addActionListener(this);
        setVisible(true);
    }

 
  public void actionPerformed(ActionEvent ae){
      setVisible(false);
      new Login();
      
  }
    
    
    public static void main(String[] args) {
        new HotelManagementSystem();
        
    }   
}
