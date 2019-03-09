import React, { Component } from 'react';
import SelectComponent from './SelectComponent';
import { DONE, LOADING } from './SelectConstants';
import configs from '../configs';
import { makeRequest } from '../util/Request';

const { API_BASE, NODE_ENV } = configs;

function withDataHandlers(WrappedComponent) {
  return class extends Component {
    constructor(props) {
      super(props);
      this.state = {
        data: [],
        status: LOADING
      };
    }

    componentDidMount() {
      this.fetchData();
    }

    fetchData = async () => {
      const { payload } = await makeRequest(`${API_BASE}/v1/symptoms`);
      this.setState({ data: payload, status: DONE });
    }

    render() {
      const { data, status } = this.state;
      return <WrappedComponent data={data} status={status} {...this.props} />;
    }
  };
}

export default withDataHandlers(SelectComponent);
