package presentatie;

import logica.Klasgroep;
import logica.Rapport;
import logica.Vak;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class OpleidingGUI {
    private JPanel mainPanel;
    private JPanel Rapport;
    private JLabel vakNaam1;
    private JLabel vakNaam2;
    private JLabel vakNaam3;
    private JLabel vakNaam4;
    private JLabel vakNaam5;
    private JLabel vakNaam6;
    private JTextField punten1;
    private JTextField punten2;
    private JTextField punten3;
    private JTextField punten5;
    private JTextField punten6;
    private JTextField punten4;
    private JLabel MaxScore;
    private JLabel Resultaat;
    private JTextField studentennummer;
    private JButton addButton;
    private JButton verwijderButton;
    private JComboBox klasgroep;
    private JComboBox comboBox2;
    private JPanel studenten;
    private JPanel StudentManager;
    private JTextField naam;


    private JLabel[] vakken = {vakNaam1, vakNaam2, vakNaam3, vakNaam4, vakNaam5, vakNaam6};
    private JTextField[] punten = {punten1, punten2, punten3, punten4, punten5, punten6};
    private logica.Rapport rapport = new Rapport();

    private int aantalVakken;







    private void controlePunten(int index){
        try{
            int score = Integer.parseInt(punten[index].getText());
            rapport.getVakken()[index].setScore(score);

            if(rapport.getVakken()[index].getScore() >= 10){
                punten[index].setBackground(Color.green);
            }else{
                punten[index].setBackground(Color.orange);
            }

            boolean allesIngevuld = true;

            for (int i = 0; i < aantalVakken; i++) {
                if (punten[i].getText() == null || punten[i].getText().isEmpty()) allesIngevuld = false;
            }

            if (allesIngevuld){
                Resultaat.setText("Resultaat: " + rapport.toString());
            }
        }catch (IllegalArgumentException e){
            punten[index].setBackground(Color.red);
            Resultaat.setText("Score moet in  bereik [0,20] liggen");
            Resultaat.setForeground(Color.red);
        }


    }

    public OpleidingGUI() {
        klasgroep.setModel(new DefaultComboBoxModel(Klasgroep.values()));


        rapport.setVakken(new Vak[]{new Vak("code_EN", "Elektronische Netwerken", 6), new Vak("code_PF", "Programming Fundamentals", 6), new Vak("code_WI", "Web Introduction", 6), new Vak("code_IF", "Infrastructure Fundamentals", 6), new Vak("code_ER", "Elektronische Realisatietechnieken", 6), new Vak("code_FSI", "Fundamental Skills for ICT", 6) });


        //rapport.setVakken(new Vak[]{new Vak("code_EN", "Elektronische Netwerken", 6), new Vak("code_PF", "Programming Fundamentals", 6)});

        aantalVakken = rapport.getVakken().length;

        MaxScore.setText("Max Score: " + String.valueOf(Vak.MAX_SCORE));

        int i;
        for (i = 0; i < aantalVakken; i++) {
            vakken[i].setText(rapport.getVakken()[i].getNaam());
            vakken[i].setVisible(true);
            punten[i].setVisible(true);
        }

        for (; i < vakken.length; i++) {
            vakken[i].setVisible(false);
            punten[i].setVisible(false);
        }


        punten1.addActionListener(e -> controlePunten(0));
        punten2.addActionListener(e -> controlePunten(1));
        punten3.addActionListener(e -> controlePunten(2));
        punten4.addActionListener(e -> controlePunten(3));
        punten5.addActionListener(e -> controlePunten(4));
        punten6.addActionListener(e -> controlePunten(5));


        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("OpleidingGUI");
        frame.setContentPane(new OpleidingGUI().mainPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500,500);
        frame.setVisible(true);
    }
}
