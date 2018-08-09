package com.github.nettybook.ch9.core;

/**
 * Created by SunMyeong Lee on 2018-08-07.
 */
import java.util.Map;

import com.github.nettybook.ch9.service.RequestParamException;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

@Service("notFound")
@Scope("prototype")
public class DefaultApiRequest extends ApiRequestTemplate {

    public DefaultApiRequest(Map<String, String> reqData) {
        super(reqData);
    }

    @Override
    public void requestParamValidation() throws RequestParamException {

    }

    @Override
    public void service() {
        this.apiResult.addProperty("resultCode", "404");
    }

    @Override
    public void executeService() {

    }
}