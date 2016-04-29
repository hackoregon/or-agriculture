import React, { Component } from 'react';

export default class DropDown extends Component {
  render() {
    return (
      <div className="drop-down">
        <select name="crops">
          <option>Crop 1</option>
        </select>
      </div>
    );
  }
}
