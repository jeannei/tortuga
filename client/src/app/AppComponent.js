import React, { Component } from 'react';
import PropTypes from 'prop-types';
import styles from './App.css';
import SelectComponent from '../select/SelectContainer';

export default class AppComponent extends Component {
  static propTypes = {
    data: PropTypes.array,
    status: PropTypes.string,
    selectedValue: PropTypes.object,
    handleSelectChange: PropTypes.func.isRequired
  }

  renderTopDiagnosis() {

  }

  render() {
    const { handleSelectChange, selectedValue, data } = this.props;
    console.log(data);
    return (
      <div className={styles.app}>
        <SelectComponent label={"Sympom Selector"} handleChange={handleSelectChange} />
      </div>
    );
  }
}
