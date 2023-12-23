const { authJwt } = require("../middleware/index.js");
const foods = require("../controllers/food.controller.js");

module.exports = (app) => {
    var router = require("express").Router();

    router.post("/", [authJwt.verifyToken], foods.create);
    router.get("/", [authJwt.verifyToken], foods.findAll);
    router.get("/:id", [authJwt.verifyToken], foods.findOne);
    router.put("/:id", [authJwt.verifyToken], foods.update);
    router.delete("/:id", [authJwt.verifyToken], foods.delete);
    // router.delete("/", [authJwt.verifyToken], foods.deleteAll);

    app.use('/api/foods', router);
};
