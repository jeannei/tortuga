import React, { Component } from 'react';
import AppComponent from './AppComponent';
import { DONE, LOADING } from './AppConstants';
import configs from '../configs';
import { makeRequest } from '../util/Request';
import { DETERMINED, NOT_DETERMINED, PENDING } from './AppConstants';

const { API_BASE } = configs;
const INITIAL_STATE = {
  diagnoses: [],
  diagnosisStatus: NOT_DETERMINED,
  isDialogOpen: false,
  selectedSymptom: {},
  status: DONE
};

function withDataHandlers(WrappedComponent) {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = INITIAL_STATE;
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
      this.setState({ isDialogOpen: false, diagnosisStatus: PENDING });
    };

    handleCloseDialogConfirm = (diagnosis) => {
      this.confirmDiagnosis(diagnosis);
      this.setState({ isDialogOpen: false, diagnosisStatus: DETERMINED });
    }

    handleDiagnosisSlector = (diagnosis) => {
      this.confirmDiagnosis(diagnosis);
      this.setState({ diagnosisStatus: DETERMINED });
    }

    handleRefresh = () => {
      this.setState(INITIAL_STATE);
    }

    handleSelectChange = (value) => {
      this.setState({ selectedSymptom: value });
      this.fetchDiagnoses(value.id);
    }

    _sortDescending(array) {
      array.sort((a, b) => b.frequency - a.frequency);
    }

    render() {
      const { diagnoses, diagnosisStatus, isDialogOpen, status, selectedSymptom } = this.state;
      return <WrappedComponent
        confirmDiagnosis={this.confirmDiagnosis}
        diagnoses={diagnoses}
        handleCloseDialog={this.handleCloseDialog}
        handleCloseDialogConfirm={this.handleCloseDialogConfirm}
        handleDiagnosisSlector={this.handleDiagnosisSlector}
        handleRefresh={this.handleRefresh}
        handleSelectChange={this.handleSelectChange}
        diagnosisStatus={diagnosisStatus}
        isDialogOpen={isDialogOpen}
        status={status}
        selectedSymptom={selectedSymptom}
        {...this.props}
      />;
    }
  };
}

export default withDataHandlers(AppComponent);
