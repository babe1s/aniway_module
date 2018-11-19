odoo.define('kikadu_pos_stock.models', function (require) {

    "use strict";

    var models = require('point_of_sale.models');

    models.load_fields('product.product', ['x_brand']);



});