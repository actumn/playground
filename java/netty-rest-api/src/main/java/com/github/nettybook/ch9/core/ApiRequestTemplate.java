package com.github.nettybook.ch9.core;

import com.github.nettybook.ch9.service.RequestParamException;
import com.github.nettybook.ch9.service.ServiceException;
import com.google.gson.JsonObject;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Map;

/**
 * Created by SunMyeong Lee on 2018-08-07.
 */
public abstract class ApiRequestTemplate implements ApiRequest {
    protected Logger logger;

    protected Map<String, String> reqData;

    protected JsonObject apiResult;

    public ApiRequestTemplate(Map<String, String> reqData) {
        this.logger = LogManager.getLogger(this.getClass());
        this.apiResult = new JsonObject();
        this.reqData = reqData;

        logger.info("request data: "+ this.reqData);
    }

    public void executeSerivce() {
        try {
            this.requestParamValidation();
            this.service();
        }
        catch (RequestParamException e) {
            logger.error(e);
            this.apiResult.addProperty("resultCode", "405");
        }
        catch (ServiceException e) {
            logger.error(e);
            this.apiResult.addProperty("resultCode", "501");
        }
    }

    public JsonObject getApiResult() {
        return apiResult;
    }
}
