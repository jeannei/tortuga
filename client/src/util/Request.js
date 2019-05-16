import request from 'request';
import ApiError from './ApiError';

export function makeRequest(url, params = {}, method = 'GET') {
  return new Promise((resolve, reject) => {
    request({ method, url, ...params }, (error, response, body) => {
      if (error) {
        reject(new ApiError(response, body, error));
        return;
      }

      const { statusCode } = response;
      if (!(statusCode >= 200 && statusCode < 300)) {
        reject(new ApiError(response, body));
        return;
      }

      let payload = body;
      try {
        payload = JSON.parse(body);
      } catch (e) {}

      resolve({ response, payload });
    });
  });
}
