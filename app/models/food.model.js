module.exports = (sequelize, Sequelize) => {
    const Food = sequelize.define("foods", {
        nama_makanan: {
            type: Sequelize.STRING
        },
        kalori_kcal: {
            type: Sequelize.FLOAT
        },
        kolestrol_mg: {
            type: Sequelize.INTEGER
        },
        lemak_g: {
            type: Sequelize.FLOAT
        },
        karbohidrat_g: {
            type: Sequelize.FLOAT
        },
        protein_g: {
            type: Sequelize.FLOAT
        },
        kalium_mg: {
            type: Sequelize.INTEGER
        },
        nutrisi: {
            type: Sequelize.STRING
        },
        ingredient: {
            type: Sequelize.TEXT
        },
    });

    return Food;
};