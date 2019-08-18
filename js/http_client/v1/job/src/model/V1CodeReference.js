// Copyright 2019 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * Job service
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.7
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.JobService) {
      root.JobService = {};
    }
    root.JobService.V1CodeReference = factory(root.JobService.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The V1CodeReference model module.
   * @module model/V1CodeReference
   * @version 1.0
   */

  /**
   * Constructs a new <code>V1CodeReference</code>.
   * @alias module:model/V1CodeReference
   * @class
   */
  var exports = function() {
    var _this = this;








  };

  /**
   * Constructs a <code>V1CodeReference</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/V1CodeReference} obj Optional instance to populate.
   * @return {module:model/V1CodeReference} The populated <code>V1CodeReference</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'String');
      }
      if (data.hasOwnProperty('uuid')) {
        obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
      }
      if (data.hasOwnProperty('commit')) {
        obj['commit'] = ApiClient.convertToType(data['commit'], 'String');
      }
      if (data.hasOwnProperty('updated_at')) {
        obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
      }
      if (data.hasOwnProperty('status')) {
        obj['status'] = ApiClient.convertToType(data['status'], 'String');
      }
      if (data.hasOwnProperty('git_url')) {
        obj['git_url'] = ApiClient.convertToType(data['git_url'], 'String');
      }
      if (data.hasOwnProperty('is_dirty')) {
        obj['is_dirty'] = ApiClient.convertToType(data['is_dirty'], 'Boolean');
      }
    }
    return obj;
  }

  /**
   * @member {String} id
   */
  exports.prototype['id'] = undefined;
  /**
   * @member {String} uuid
   */
  exports.prototype['uuid'] = undefined;
  /**
   * @member {String} commit
   */
  exports.prototype['commit'] = undefined;
  /**
   * @member {String} updated_at
   */
  exports.prototype['updated_at'] = undefined;
  /**
   * @member {String} status
   */
  exports.prototype['status'] = undefined;
  /**
   * @member {String} git_url
   */
  exports.prototype['git_url'] = undefined;
  /**
   * @member {Boolean} is_dirty
   */
  exports.prototype['is_dirty'] = undefined;



  return exports;
}));


