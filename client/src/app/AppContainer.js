import React, { Component } from 'react';
import AppComponent from './AppComponent';
import { DONE, LOADING } from './AppConstants';
import configs from '../configs';
import { makeRequest } from '../util/Request';

const { API_BASE } = configs;

function withDataHandlers(WrappedComponent) {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        selectedValue: null,
        diagnoses: [],
        status: DONE
      };
    }

    confirmDiagnosis = async (diagnosis) => {
      const { selectedValue, diagnoses } = this.state;
      const { id } = diagnosis;
      const sid = selectedValue.id;
      const tempData = diagnoses.filter(item => item.id !== id);
      const newData = [...newData, {...diagnosis, frequency: diagnosis.frequency + 1 }];

      this._sortDescending(newData);
      this.setState({ diagnoses: newData});
      const { payload } = await makeRequest(`${API_BASE}/v1/symptoms/${sid}/diagnoses/${id}/confirm`);
    }

    fetchData = async (sid) => {
      const { payload } = await makeRequest(`${API_BASE}/v1/symptoms/${sid}/diagnoses`);
      this._sortDescending(payload);
      this.setState({ diagnoses: payload, status: DONE });
    }

    handleSelectChange = (value) => {
      this.setState({ selectedValue: value });
      this.fetchData(value.id);
    }

    _sortDescending(array) {
      array.sort((a, b) => b.frequency - a.frequency);
    }

    render() {
      const { diagnoses, status, selectedValue } = this.state;
      return <WrappedComponent
        data={diagnoses}
        status={status}
        selectedValue={selectedValue}
        handleSelectChange={this.handleSelectChange}
        {...this.props}
      />;
    }
  };
}

export default withDataHandlers(AppComponent);
