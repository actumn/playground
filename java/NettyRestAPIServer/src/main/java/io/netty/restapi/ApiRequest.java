package io.netty.restapi;

import com.google.gson.JsonObject;

/**
 * Created by SunMyeong Lee on 2016-08-31.
 */
public interface ApiRequest {
    public void requestParamValidation() throws RequestParamException;

    public void service() throws ServiceException;

    public void executeService();

    public JsonObject getApiResult();
}
