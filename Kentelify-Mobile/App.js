import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.labels}>Kentelify</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#044075',
    alignItems: 'center',
    justifyContent: 'center',
    color:"#2fea0e",
  },
  labels:{
    flex:1,
    position:"fixed",
    top:"30%",
    fontSize:"40px",
    fontFamily:"Monospace",
    color:"#2fea0e",
  }
});
