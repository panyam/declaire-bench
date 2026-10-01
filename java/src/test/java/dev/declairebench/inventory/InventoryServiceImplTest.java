package dev.declairebench.inventory;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import dev.declairebench.inventory.v1.Item;
import dev.declairebench.inventory.v1.ReserveItemRequest;
import dev.declairebench.inventory.v1.ReserveItemResponse;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import java.util.List;
import org.junit.jupiter.api.Test;

class InventoryServiceImplTest {
  private final InventoryServiceImpl service =
      new InventoryServiceImpl(
          List.of(Item.newBuilder().setSku("sku-1").setName("Widget").setOnHand(5).build()));

  @Test
  void reserveItemTakesFromStock() {
    Recorder<ReserveItemResponse> got = new Recorder<>();
    service.reserveItem(reserve("order-1", "sku-1", 3), got);
    assertNull(got.error);
    assertEquals(2, got.value.getRemaining());
    assertEquals("order-1-1", got.value.getReservationId());
  }

  @Test
  void reserveItemRefusesMoreThanOnHand() {
    Recorder<ReserveItemResponse> got = new Recorder<>();
    service.reserveItem(reserve("order-1", "sku-1", 6), got);
    assertEquals(Status.Code.FAILED_PRECONDITION, Status.fromThrowable(got.error).getCode());
  }

  @Test
  void reserveItemRefusesUnknownSku() {
    Recorder<ReserveItemResponse> got = new Recorder<>();
    service.reserveItem(reserve("order-1", "sku-9", 1), got);
    assertEquals(Status.Code.NOT_FOUND, Status.fromThrowable(got.error).getCode());
  }

  private static ReserveItemRequest reserve(String order, String sku, int quantity) {
    return ReserveItemRequest.newBuilder()
        .setOrderId(order)
        .setSku(sku)
        .setQuantity(quantity)
        .build();
  }

  private static final class Recorder<T> implements StreamObserver<T> {
    T value;
    Throwable error;

    @Override
    public void onNext(T v) {
      value = v;
    }

    @Override
    public void onError(Throwable t) {
      error = t;
    }

    @Override
    public void onCompleted() {}
  }
}
