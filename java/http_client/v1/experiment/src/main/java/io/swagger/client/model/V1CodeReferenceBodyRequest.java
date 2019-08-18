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

/*
 * Experiment service
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.V1CodeReference;
import io.swagger.client.model.V1OwnedEntityIdRequest;
import java.io.IOException;

/**
 * V1CodeReferenceBodyRequest
 */

public class V1CodeReferenceBodyRequest {
  @SerializedName("entity")
  private V1OwnedEntityIdRequest entity = null;

  @SerializedName("CodeReference")
  private V1CodeReference codeReference = null;

  public V1CodeReferenceBodyRequest entity(V1OwnedEntityIdRequest entity) {
    this.entity = entity;
    return this;
  }

   /**
   * Get entity
   * @return entity
  **/
  @ApiModelProperty(value = "")
  public V1OwnedEntityIdRequest getEntity() {
    return entity;
  }

  public void setEntity(V1OwnedEntityIdRequest entity) {
    this.entity = entity;
  }

  public V1CodeReferenceBodyRequest codeReference(V1CodeReference codeReference) {
    this.codeReference = codeReference;
    return this;
  }

   /**
   * Get codeReference
   * @return codeReference
  **/
  @ApiModelProperty(value = "")
  public V1CodeReference getCodeReference() {
    return codeReference;
  }

  public void setCodeReference(V1CodeReference codeReference) {
    this.codeReference = codeReference;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1CodeReferenceBodyRequest v1CodeReferenceBodyRequest = (V1CodeReferenceBodyRequest) o;
    return Objects.equals(this.entity, v1CodeReferenceBodyRequest.entity) &&
        Objects.equals(this.codeReference, v1CodeReferenceBodyRequest.codeReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entity, codeReference);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1CodeReferenceBodyRequest {\n");
    
    sb.append("    entity: ").append(toIndentedString(entity)).append("\n");
    sb.append("    codeReference: ").append(toIndentedString(codeReference)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

