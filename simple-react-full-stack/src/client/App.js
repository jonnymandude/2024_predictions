import React, { Component } from 'react';
import './app.css';
import ReactImage from './react.png';
import {LineChart} from 'recharts';

export default class App extends Component {
  state = { marketData: null };

  componentDidMount() {
    fetch('/api/getData')
      .then(res => res.json())
      .then(data => this.setState({ marketData: data }));
  }

// Send the response
  render() {
    const { marketData } = this.state;
    console.log(marketData);

    const markets = marketData != null ? marketData.map(function(datum) {return datum.market_name;}) : null;
    const uniqueMarkets = [...new Set(markets)]
    console.log(uniqueMarkets);

    const marketInfo =  uniqueMarkets.map(function(marketName) {
      const specificData = marketData.filter(data => data.market_name == marketName);
      console.log(specificData);

      const individualResults = specificData.map(function(individualOdds) {

      return (<h2>
        <img 
        src={individualOdds.image} 
        style={{
          width: '50px',
          height: '50px',
        }}
        alt="react" 
        />{`Option: ${marketName}`}{individualOdds.name} - Current Price: ${individualOdds.price} as of {individualOdds.timestamp}</h2>)
      })
    
      return (
      <div
      style={{
        outlineStyle: 'dashed',
        padding: '20px',
        margin: '20px',
        borderRadius: '4px',
        textAlign: 'center',
        verticalAlign: 'center',
        }}>
        <h1><img 
        src={specificData[0].market_image} 
        style={{
          width: '100px',
          height: '100px',
        }}
        alt="react" 
        />{`Market: ${marketName}`}</h1>
        {individualResults}
      </div>);
    })



    return (
      <div>
        {marketData != null ? marketInfo : <h1>Loading.. please wait!</h1>}
      </div>
    );
  }
}
