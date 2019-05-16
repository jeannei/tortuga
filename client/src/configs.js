const NODE_ENV = (process.env.NODE_ENV || 'development');
const configs = require(`../envs/${NODE_ENV}`);

export default { ...configs, NODE_ENV };
