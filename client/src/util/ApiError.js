export default class ApiError extends Error {
  constructor(response = {}, payload = {}, ...params) {
    // Pass remaining arguments (including vendor specific ones) to parent constructor
    super(...params);

    // Maintains proper stack trace for where our error was thrown (only available on V8)
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(this, ApiError);
    }

    this.response = response;
    this.payload = payload;
    this.date = new Date();
  }
}
