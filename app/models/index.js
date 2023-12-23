const config = require("../config/db.config.js");

const Sequelize = require("sequelize");
const sequelize = new Sequelize(
  config.DB,
  config.USER,
  config.PASSWORD,
  {
    host: config.HOST,
    dialect: config.dialect,
    pool: {
      max: config.pool.max,
      min: config.pool.min,
      acquire: config.pool.acquire,
      idle: config.pool.idle
    }
  }
);

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.user = require("../models/user.model.js")(sequelize, Sequelize);
db.role = require("../models/role.model.js")(sequelize, Sequelize);
db.foods = require("./food.model.js")(sequelize, Sequelize);

db.user.belongsToMany(db.role, {
  through: {
    model: "user_roles",
    timestamps: true,
    createdAt: 'createdAt',
    updatedAt: 'updatedAt',
  },
  foreignKey: 'user_id',
});
db.role.belongsToMany(db.user, {
  through: {
    model: "user_roles",
    timestamps: true,
    createdAt: 'createdAt',
    updatedAt: 'updatedAt',
  },
  foreignKey: 'role_id',
});

db.ROLES = ["user", "admin", "moderator"];

module.exports = db;
