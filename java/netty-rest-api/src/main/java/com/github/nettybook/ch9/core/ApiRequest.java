package com.github.nettybook.ch9.core;

import com.github.nettybook.ch9.service.RequestParamException;
import com.github.nettybook.ch9.service.ServiceException;
import com.google.gson.JsonObject;

/**
 * Created by SunMyeong Lee on 2018-08-07.
 */
public interface ApiRequest {
    void requestParamValidation() throws RequestParamException;

    void service() throws ServiceException;

    void executeService();

    JsonObject getApiResult();
}
