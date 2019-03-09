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
        diagnoses: [],
        isDialogOpen: false,
        selectedSymptom: {},
        status: DONE
      };
    }

    confirmDiagnosis = async (diagnosis) => {
      const { selectedSymptom, diagnoses } = this.state;
      const { id } = diagnosis;
      const sid = selectedSymptom.id;
      const tempData = diagnoses.filter(item => item.id !== id);
      const newData = [...tempData, {...diagnosis, frequency: diagnosis.frequency + 1 }];

      this._sortDescending(newData);
      this.setState({ diagnoses: newData});
      await makeRequest(`${API_BASE}/v1/symptoms/${sid}/diagnoses/${id}/confirm`, {}, 'PUT');
    }

    fetchDiagnoses = async (sid) => {
      this.setState({ status: LOADING });
      const { payload } = await makeRequest(`${API_BASE}/v1/symptoms/${sid}/diagnoses`);
      this._sortDescending(payload);
      this.setState({ diagnoses: payload, status: DONE, isDialogOpen: true });
    }

    handleCloseDialog = () => {
      this.setState({ isDialogOpen: false, accepted: false });
    };

    handleCloseDialogConfirm = (diagnosis) => {
      this.confirmDiagnosis(diagnosis);
      this.setState({ isDialogOpen: false, accepted: true });
    }

    handleSelectChange = (value) => {
      this.setState({ selectedSymptom: value });
      this.fetchDiagnoses(value.id);
    }

    _sortDescending(array) {
      array.sort((a, b) => b.frequency - a.frequency);
    }

    render() {
      const { diagnoses, isDialogOpen, status, selectedSymptom } = this.state;
      return <WrappedComponent
        confirmDiagnosis={this.confirmDiagnosis}
        diagnoses={diagnoses}
        handleCloseDialog={this.handleCloseDialog}
        handleCloseDialogConfirm={this.handleCloseDialogConfirm}
        handleSelectChange={this.handleSelectChange}
        isDialogOpen={isDialogOpen}
        status={status}
        selectedSymptom={selectedSymptom}
        {...this.props}
      />;
    }
  };
}

export default withDataHandlers(AppComponent);
