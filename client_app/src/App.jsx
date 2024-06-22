import React from 'react';
import ContactForm from './view/ContactForm';

const App = () => {
  return (
    <div>
      <h1 style={styles.header}>Formulario de Contacto</h1>
      <ContactForm  />
    </div>
  );
};

const styles = {
  header: {
    textAlign: 'center',
    margin: '20px 0',
    fontFamily: 'Arial, sans-serif'
  }
};

export default App;
