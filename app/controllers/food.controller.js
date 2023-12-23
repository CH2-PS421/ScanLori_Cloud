const db = require("../models");
const Food = db.foods;
const Op = db.Sequelize.Op;

exports.create = (req, res) => {
    if (!req.body.nama_makanan) {
        res.status(400).send({
            message: "Content can not be empty!"
        });
        return;
    }

    const food = {
        nama_makanan: req.body.nama_makanan,
        kalori_kcal: req.body.kalori_kcal,
        kolestrol_mg: req.body.kolestrol_mg,
        lemak_g: req.body.lemak_g,
        karbohidrat_g: req.body.karbohidrat_g,
        protein_g: req.body.protein_g,
        kalium_mg: req.body.kalium_mg,
        nutrisi: req.body.nutrisi,
        ingredient: req.body.ingredient,
    };

    Food.create(food)
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while creating the Food."
            });
        });
};

exports.findAll = (req, res) => {
    const nama_makanan = req.query.nama_makanan;
    var condition = nama_makanan ? { nama_makanan: { [Op.like]: `%${nama_makanan}%` } } : null;

    Food.findAll({ where: condition })
        .then(data => {
            res.send(data);
        })
        .catch(err => {
            res.status(500).send({
                message:
                    err.message || "Some error occurred while retrieving Foods."
            });
        });
};

exports.findOne = (req, res) => {
    const id = req.params.id;

    Food.findByPk(id)
        .then(data => {
            if (data) {
                res.send(data);
            } else {
                res.status(404).send({
                    message: `Cannot find Food with id=${id}.`
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Error retrieving Food with id=" + id
            });
        });
};

exports.update = (req, res) => {
    const id = req.params.id;

    Food.update(req.body, {
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.send({
                    message: "Food was updated successfully."
                });
            } else {
                res.send({
                    message: `Cannot update Food with id=${id}. Maybe Food was not found or req.body is empty!`
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Error updating Food with id=" + id
            });
        });
};

exports.delete = (req, res) => {
    const id = req.params.id;

    Food.destroy({
        where: { id: id }
    })
        .then(num => {
            if (num == 1) {
                res.send({
                    message: "Food was deleted successfully!"
                });
            } else {
                res.send({
                    message: `Cannot delete Food with id=${id}. Maybe Food was not found!`
                });
            }
        })
        .catch(err => {
            res.status(500).send({
                message: "Could not delete Food with id=" + id
            });
        });
};

// exports.deleteAll = (req, res) => {
//     Food.destroy({
//         where: {},
//         truncate: false
//     })
//         .then(nums => {
//             res.send({ message: `${nums} Foods were deleted successfully!` });
//         })
//         .catch(err => {
//             res.status(500).send({
//                 message:
//                     err.message || "Some error occurred while removing all Foods."
//             });
//         });
// };