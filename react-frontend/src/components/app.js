import React from 'react';
import { Component } from 'react';

import DropDown from './drop_down'

export default class App extends Component {
  render() {
    return (
      <div>
        <h1>Crop Compass</h1>
        <DropDown />
      </div>
    );
  }
}
